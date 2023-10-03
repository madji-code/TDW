from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mpaf/home.html', {'logged_in': request.user.is_authenticated, 'back_page': 'mpaf:home'})