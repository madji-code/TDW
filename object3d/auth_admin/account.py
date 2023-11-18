from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


User = get_user_model()

@login_required
def account(request):
    return render(request, "auth_admin/account.html")

