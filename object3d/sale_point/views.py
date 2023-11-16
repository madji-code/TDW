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

import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Customer, Cart, Product, Price

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




 
stripe.api_key = settings.STRIPE_SECRET_KEY
 
 
class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        domain = "https://3dw.madji.org"
        if settings.DEBUG:
            domain = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'cad',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stupi name',
                            'images': ['https://shorturl.at/bhoFO']
                        },
                    }
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )
        return redirect(checkout_session.url)
    

class SuccessView(TemplateView):
    template_name = "success.html"
 
class CancelView(TemplateView):
    template_name = "cancel.html"


class ProductLandingPageView(TemplateView):
    template_name = "landing.html"
 
    def get_context_data(self, **kwargs):
        product = Product.objects.get(name="Test Product")
        prices = Price.objects.filter(product=product)
        context = super(ProductLandingPageView,
                        self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "prices": prices
        })
        return context