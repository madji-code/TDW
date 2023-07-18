from django.urls import path
from . import views

urlpatterns = [
    path('view-objects', views.view_objects, name="view-objects"),
    path('view-this-object/<int:id>', views.view_this_object, name="view-this-object"),
]

