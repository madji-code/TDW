'''
Views.py
- Toutes les pages du système de vente d'objects 3d.
'''
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth.models import AnonymousUser

from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model



from .models import Customer, Cart, Product

User = get_user_model()


# Views
def home(request):
    print(request.user.is_authenticated)
    return render(request, "sale_point/home.html", {'logged_in': request.user.is_authenticated, "back_page": 'sale_point:home', "acceuil":'active'})



def view_products(request):
    '''- Voir tous les produits 3d'''
    all_objects = Product.objects.all()
        
    return render(request, "sale_point/view-objects.html", {'all_objects': all_objects, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products', "boutique":'active'})


def view_this_product(request, id):
    this_object = Product.objects.get(id=id)
    return render(request, "sale_point/view-this-object.html", {'this_object': this_object, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products'})


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
        products_id = cart.products
        objects = [Product.objects.get(id=product_id) for product_id in products_id]

    return render(request, "sale_point/cart.html", {'logged_in': request.user.is_authenticated, "objects": objects, 'back_page': 'sale_point:cart'})

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
