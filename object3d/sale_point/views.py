'''
Views.py
- Toutes les pages du système de vente d'objects 3d.
'''
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model


from .models import Product, Cart

User = get_user_model()


# Views
def home(request):
    print(request.user.is_authenticated)
    return render(request, "sale_point/home.html", {'logged_in': request.user.is_authenticated})


@login_required(login_url='sale_point:login_user')
def panier(request):
    return render(request, f"sale_point/panier.html", {'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:panier'})


def view_products(request):
    '''- Voir tous les produits 3d'''
    all_objects = Product.objects.all()

    # products_list = []
    # n = 0
    # i = 0
    # print('ok')
    # for object in all_objects:
    #     if n == 4:
    #         n = 0
    #         i += 1
    #     if n > 0:
    #         products_list[i].append(object)
    #     else:
    #         products_list.append([object])  
        # n += 1
        
        
    return render(request, "sale_point/view-objects.html", {'all_objects': all_objects, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products'})


def view_this_product(request, id):
    this_object = Product.objects.get(id=id)
    return render(request, "sale_point/view-this-object.html", {'this_object': this_object, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-this-product'})

