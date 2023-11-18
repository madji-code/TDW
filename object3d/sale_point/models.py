from django.db import models
from django_mysql.models import ListCharField
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class Cart(models.Model):
    # session_key = models.CharField(max_length=32, blank=True, null=True)
    products = ListCharField(base_field=models.IntegerField(), size=None, max_length=1000000000, default=[])

# Create your models here.
class Product(models.Model):
    name = models.CharField("Name", max_length=120)
    dimension = models.CharField("Dimension", max_length=150)
    description = models.TextField("Description", max_length=1000,  default="Object description not available!")
    creation_date = models.DateTimeField(auto_now_add=True)

    price = models.IntegerField(default=0)  # cents
    image = models.ImageField(upload_to ='static/img/%Y/', default="static/img/default/default_product.png")

    def __str__(self): 
        return f"ID:{self.id}  -  NAME:{self.name}  -  PRICE:{self.price}  -  DATE{self.creation_date}"

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
    
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    
