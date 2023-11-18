from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Product
User = get_user_model()


# Views
def home(request):
    print(request.user.is_authenticated)
    return render(request, "sale_point/home.html", {'logged_in': request.user.is_authenticated, "back_page": 'sale_point:home', "acceuil":'active'})



def view_products(request):
    '''- Voir tous les produits 3d'''
    all_products = [product for product in Product.objects.all() if product.name != 'DELETED']
        
    return render(request, "sale_point/view-products.html", {'all_products': all_products, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products', "boutique":'active'})


def view_this_product(request, id):
    this_product = Product.objects.get(id=id)
    return render(request, "sale_point/view-this-product.html", {'this_product': this_product, 'logged_in': request.user.is_authenticated, 'back_page': 'sale_point:view-products'})




