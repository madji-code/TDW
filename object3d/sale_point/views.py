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



from .models import Product, Cart

User = get_user_model()


# Views
def home(request):
    print(request.user.is_authenticated)
    return render(request, "sale_point/home.html", {'logged_in': request.user.is_authenticated})



def view_products(request):
    '''- Voir tous les produits 3d'''
    all_objects = Product.objects.all()
        
    return render(request, "sale_point/view-objects.html", {'all_objects': all_objects, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products'})


def view_this_product(request, id):
    this_object = Product.objects.get(id=id)
    return render(request, "sale_point/view-this-object.html", {'this_object': this_object, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-this-product'})



def cart(request):
    # Get the current session key
    session_key = request.session.session_key

    # Check if the user is anonymous
    if not request.user.is_authenticated and session_key is not None:
        try:
            cart = Cart.objects.get(session_key=session_key, customer=AnonymousUser())
            # Display the cart for this anonymous user
            return render(request, f"sale_point/cart.html", {'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:cart', 'cart': cart,})
        except Cart.DoesNotExist:
            raise Http404("Cart does not exist or you don't have permission to view it.")
    else:
        pass# Handle cases for authenticated users (if needed)
    return render(request, f"sale_point/cart.html", {'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:cart'})

def add_to_cart(request, product_id, next):
    product = Product.objects.get(id=product_id)
    
    # Get the current session key
    session_key = request.session.session_key
    print(session_key)

    # Check if the user is anonymous
    if not request.user.is_authenticated and session_key is not None:
        # Find or create a cart associated with the session key
        cart, created = Cart.objects.get_or_create(session_key=session_key, customer=AnonymousUser())
        cart.products.add(product)
        cart.save()

    else:
        pass
    

    return redirect(reverse(next))