from django.urls import path
from . import views

app_name='sale_point'

urlpatterns = [
    path('', views.home, name="home"),
    path('boutique', views.view_products, name="view-products"),
    path('view-this-product/<int:id>', views.view_this_product, name="view-this-product"),
    path('cart/', views.cart, name="cart"),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name="add-to-cart"),
    path('add-to-cart-success/<int:product_id>', views.add_to_cart_success, name="add-to-cart-success"),
]
