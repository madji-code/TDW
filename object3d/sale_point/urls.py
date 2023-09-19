from django.urls import path
from . import views

app_name='sale_point'

urlpatterns = [
    path('home', views.home, name="home"),

    path('', views.view_objects, name="view-objects"),
    path('view-this-object/<int:id>', views.view_this_object, name="view-this-object"),
    path('panier/', views.panier, name="panier"),
]
