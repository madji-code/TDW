from django.db import models

# Create your models here.
class Object(models.Model):
    name = models.CharField("Object", max_length=120)

    def __str__(self): 
        return self.name