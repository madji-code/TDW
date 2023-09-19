from django.urls import path
from . import views

app_name='auth_admin'

urlpatterns = [
    path('<str:next>', views.login_user, name="login_user"),
    path('logout/<str:next>', views.logout_user, name="logout_user"),
    path('register/<str:next>', views.register, name="register"),

]
