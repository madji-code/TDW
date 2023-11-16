from django.contrib import admin
from .models import Product, Cart, Customer, Price
# Register your models here.
admin.site.register(Product)
admin.site.register(Price)

admin.site.register(Customer)
admin.site.register(Cart)