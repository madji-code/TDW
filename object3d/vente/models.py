from django.db import models

# Create your models here.
class Object(models.Model):
    name = models.CharField("Name", max_length=120)
    dimension = models.CharField("Dimension", max_length=150)
    description = models.TextField("Description", max_length=1000,  default="Object description not available!")
    creation_date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField('Price')
    image = models.ImageField(upload_to ='static/img/%Y/%m/%d/',
                              default="C:\\Users\\berth\\3D Objects\\3DW\\object3d\\vente\\static\\img\\2023\\07\\19\\support_main.PNG")

    def __str__(self): 
        return f"{self.name} - {self.creation_date} - {self.dimension} - {self.price}"
    
    
class User(models.Model):
    '''
    username, firstname, lastname, email, phone, password, rpassword
    '''
    username = models.CharField("Nom d'utilisateur", max_length=100, blank = False, null = False)
    firstname = models.CharField("Prénom", max_length=100, blank = False, null = False)
    lastname = models.CharField("Nom de famille", max_length=100, blank = False, null = False)
    email = models.EmailField("Email", max_length=100, blank = False, null = False)
    phone = models.CharField("Téléphone", max_length=100, blank = False, null = False)
    password = models.CharField("Entrez votre mot de passe", max_length=150, blank = False, null = False)
    rpassword = models.CharField("Entrez à nouveau votre mot de passe", max_length=150, null = True)

    def __str__(self): 
        return f"{self.username} - {self.email} - {self.phone}"
    
