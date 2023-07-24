'''
Views.py
- Toutes les pages du système de vente d'objects 3d.
'''
from django.shortcuts import render, HttpResponse
from .models import Object
from .forms import ConnexionForm, CreateAccountForm

# Create your views here.
def home(request):
    return render(request, "vente/home.html")


def panier(request, user_id):
    return render(request, "vente/panier.html")


def view_objects(request):
    '''- Voir tous les produits 3d'''
    all_objects = Object.objects.all()
    return render(request, "vente/view-objects.html", {'all_objects': all_objects})


def view_this_object(request, id):
    this_object = Object.objects.get(id=id)
    return render(request, "vente/view-this-object.html", {'this_object': this_object})


def connexion(request):  
    return render(request, "vente/connexion.html", {})

def create_account(request):
    # check if the request is post
    if request.method =='POST': 
 
        # Pass the form data to the form class
        data = CreateAccountForm(request.POST)
 
        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if data.is_valid(): 
 
            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database  
            data.save()
 
            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponse("data submitted successfully")
             
        else:
         
            # Redirect back to the same page if the data
            # was invalid
            return render(request, "vente/create-account.html", {'form':data})
    else:
 
        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = CreateAccountForm(None)  
        return render(request, "vente/create-account.html", {'form':form})