from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('view-objects', views.view_objects, name="view-objects"),
    path('view-this-object/<int:id>', views.view_this_object, name="view-this-object"),
    path('panier/<int:user_id>', views.panier, name="panier"),
    path('connexion', views.connexion, name="connexion"),
    path('create-account', views.create_account, name="create-account"),
]

