from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Customer, Cart, Product

@login_required
def cart(request):
    try:
        cart = request.user.customer.cart
    except:
        new_cart = Cart(products=[])
        new_cart.save()
        new_customer = Customer(user=request.user, cart=new_cart)
        new_customer.save()
    else:
        products = {}
        for id in cart.products:
            try:
                if products.get(id) is None:
                    products[id] = {
                        "product": Product.objects.get(id=id),
                        "quantity": 0
                    }
                products[id]["quantity"] += 1
            except:
                cart.products.remove(id)
       
        # Removes all deleted products
        cart.save()
        
        products = [products[item] for item in products]
        print(list(products))

    return render(request, "sale_point/cart.html", {'logged_in': request.user.is_authenticated, "products": products, 'back_page': 'sale_point:cart'})

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        try:
            cart = request.user.customer.cart
            print(cart)
        except:
            new_cart = Cart()
            new_cart.save()
            new_customer = Customer(user=request.user, cart=new_cart)
            new_customer.save()
        else:
            print(product_id)
            cart.products.append(product_id)
            cart.save()
    else:
        print('become a costumer')
    return redirect(reverse('sale_point:add-to-cart-success', args=[product_id]))

def add_to_cart_success(request, product_id):
    this_object = Product.objects.get(id=product_id)
    return render(request, "sale_point/add-to-cart-success.html", {'this_object': this_object, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-this-product'})

@login_required
def delete_from_cart(request, item_id):
    cart = request.user.customer.cart
    cart.products.remove(item_id)
    cart.save()
    return redirect(reverse('sale_point:cart'))