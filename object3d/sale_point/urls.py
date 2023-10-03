from django.urls import path
from . import views

app_name='sale_point'

urlpatterns = [
    path('home', views.home, name="home"),

    path('', views.view_products, name="view-products"),
    path('view-this-product/<int:id>', views.view_this_product, name="view-this-product"),
    path('panier/', views.panier, name="panier"),
]
