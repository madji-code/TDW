from django.urls import path
from .views import (
    login_user,
    logout_user,
    register
)
from .account import (
    account
)

app_name='auth_admin'

urlpatterns = [
    path('<str:next>', login_user, name="login_user"),
    path('logout/<str:next>', logout_user, name="logout_user"),
    path('register/<str:next>', register, name="register"),
    path('account/', account, name="account"),

]
