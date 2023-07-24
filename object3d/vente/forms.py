from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.hashers import make_password, check_password
from .models import User

class ConnexionForm(Form):
    
    username = forms.CharField(label="Nom d'utilisateur"), 
    password = forms.CharField(label="Mot de passe"),

    def clean(self):

        # data from the form is fetched using super function
    
        # extract the username and text field from the data
        self.username = self.cleaned_data.get('username')
        self.password = self.cleaned_data.get('password')

 
        # conditions to be met for the username length
        user = User.objects.get(username=self.username)
        if user is None:
            self._errors['username'] = self.error_class(["Nom d'utilisateur ou mot de passe invalid!"])
        else:
            if not check_password(self.password, user.password):
                self._errors['username'] = self.error_class(["Nom d'utilisateur ou mot de passe invalid!"])
            else:
                print("user connected")
 
        # return any errors if found
        return self.cleaned_data

class CreateAccountForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = User

        fields = ["firstname", "lastname", "email", "phone", "username",
                  "password", "rpassword"] 
        
        widgets = {
            "firstname": forms.TextInput(attrs={'placeholder': 'John'}), 
            "lastname": forms.TextInput(attrs={'placeholder': 'Doe'}), 
            "email": forms.TextInput(attrs={'placeholder': 'john.doe@example.com'}), 
            "phone": forms.TextInput(attrs={'placeholder': '+n (xxx) xxx-xxxx)', 'type': 'tel',
                                            'pattern': "+[0-200]{1} ([0-9]{3}) [0-9]{3}-[0-9]{4} required"}),  
            "username": forms.TextInput(attrs={'placeholder': 'johndoetofu123'}), 
            "password": forms.TextInput(attrs={'placeholder': 'RGerg&?&%652', 'type': 'password'}),  
            "rpassword": forms.TextInput(attrs={'placeholder': 'Répéter le mot de passe', 'type': 'password'}), 
        }

    def clean(self):

        # data from the form is fetched using super function
        super(CreateAccountForm, self).clean()
         
        # extract the username and text field from the data
        self.username = self.cleaned_data.get('username')
        self.firstname = self.cleaned_data.get('firstname')
        self.lastname = self.cleaned_data.get('lastname')
        self.email = self.cleaned_data.get('email')
        self.phone = self.cleaned_data.get('phone')
        self.password = self.cleaned_data.get('password')
        rpassword =  self.cleaned_data.get('rpassword')

 
        # conditions to be met for the username length
        if len(self.username) < 5:
            self._errors['username'] = self.error_class([
                'Minimum 5 characters required'])
            
        if self.password != rpassword:
            self._errors['password'] = self.error_class([
                'Mot de passe différent du premier!'])
 
        # return any errors if found
        return self.cleaned_data
    
    def save(self, commit=True):
        new_user = User(username=self.username, firstname=self.firstname, lastname=self.lastname, email=self.email, phone=self.phone, password=make_password(self.password))
        if commit:
            new_user.save()

    # def reset_fields(self, form):
    #     form.data.username = ""
    #     form.data.firstname = ""
    #     form.data.lastname = ""
    #     form.data.email = ""
    #     form.data.phone = ""
    #     form.data.password = ""
    #     form.data.rpassword = ""