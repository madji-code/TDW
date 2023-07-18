'''
Views.py
- Toutes les pages du système de vente d'objects 3d.
'''
from django.shortcuts import render

# Create your views here.
def view_objects(request):
    '''- Voir tous les produits 3d'''

    return render(request, "vente/view-objects.html", {})

def view_this_object(request):
    '''- Voir tous les produits 3d'''

    return render(request, "vente/view-this-object.html", {})