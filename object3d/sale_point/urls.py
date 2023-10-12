from django.urls import path
from . import views

app_name='sale_point'

urlpatterns = [
    path('home', views.home, name="home"),

    path('', views.view_products, name="view-products"),
    path('view-this-product/<int:id>', views.view_this_product, name="view-this-product"),
    path('cart/', views.cart, name="cart"),
    path('add-to-cart/<int:product_id>/<str:next>', views.add_to_cart, name="add-to-cart")
]
