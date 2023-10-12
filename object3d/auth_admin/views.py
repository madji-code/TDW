from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

from .forms import LoginFrom, RegisterForm

User = get_user_model()

# Create your views here.
def error_404(request, exception):
    return render(request, '404.html', {})

def login_user(request, next):
    if request.method == 'POST':
        form = LoginFrom(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if not user:
                form._errors['email'] = form.error_class(["Email ou mot de passe invalid!"])
                return render(
                    request, "auth_admin/login.html", 
                    {
                        'form':form, 
                        'logged_in': request.user.is_authenticated,
                        'back_page': next
                    })
            else:
                login(request, user)
                return redirect(reverse(next))
           
        else:
            print("Form is not valid. Check your input.")

    form = LoginFrom(None)
    print(next)
    return render(
        request, "auth_admin/login.html", 
        {
            'form':form, 'logged_in': request.user.is_authenticated,
            'back_page': next
        })

def logout_user(request, next):
    logout(request)
    
    return redirect(reverse(next))

def register(request, next):
    if request.method =='POST':
        data = RegisterForm(request.POST)
        if data.is_valid():
            user = data.save()
            login(request, user)
            return redirect(reverse(next))
        else:
            return render(request, "auth_admin/register.html", {'form':data, 'logged_in': request.user.is_authenticated, 'back_page': next})
    else:
        form = RegisterForm(None)  
        return render(
            request, "auth_admin/register.html", 
            {
                'form':form, 'logged_in': request.user.is_authenticated,
                'back_page': next
            })