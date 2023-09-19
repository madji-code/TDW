from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

# Create your models here.
class Produit(models.Model):
    name = models.CharField("Name", max_length=120)
    dimension = models.CharField("Dimension", max_length=150)
    description = models.TextField("Description", max_length=1000,  default="Object description not available!")
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField('Price')
    image = models.ImageField(upload_to ='static/img/%Y/%m/%d/',
                              default="C:\\Users\\berth\\3D Objects\\3DW\\object3d\\vente\\static\\img\\2023\\07\\19\\support_main.PNG")

    def __str__(self): 
        return f"{self.name} - {self.creation_date} - {self.dimension} - {self.price}"
    
class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cart_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    session_id = models.CharField(max_length=100)