from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, blank=True)
    session_key = models.CharField(max_length=32, blank=True, null=True)
    products = models.ManyToManyField('Product')

# Create your models here.
class Product(models.Model):
    name = models.CharField("Name", max_length=120)
    dimension = models.CharField("Dimension", max_length=150)
    description = models.TextField("Description", max_length=1000,  default="Object description not available!")
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField('Price')
    image = models.ImageField(upload_to ='static/img/%Y/%m/%d/',
                              default="C:\\Users\\berth\\3D Objects\\3DW\\object3d\\vente\\static\\img\\2023\\07\\19\\support_main.PNG")

    def __str__(self): 
        return f"{self.name} - {self.creation_date} - {self.dimension} - {self.price}"
    
