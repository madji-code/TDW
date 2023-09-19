from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginFrom(forms.Form):
    email_username = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput({'placeholder': 'email or username'}))
    password = forms.CharField(label="Mot de passe", widget=forms.TextInput({'placeholder': 'RGerg&?&%652', 'type': 'password'}))


class RegisterForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = User

        fields = ["username", "email", "password", "rpassword"] 
        
        widgets = {
            "username": forms.TextInput(attrs={'placeholder': 'johndoe123'}),
            "email": forms.TextInput(attrs={'placeholder': 'john.doe@example.com'}),
            "password": forms.TextInput(attrs={'placeholder': 'secret123', 'type': 'password'}),  
            "rpassword": forms.TextInput(attrs={'placeholder': 'Répéter le mot de passe', 'type': 'password'}), 
        }

    def clean(self):

        # data from the form is fetched using super function
        super(RegisterForm, self).clean()
         
        # extract the username and text field from the data
        self.username = self.cleaned_data.get('username')
        self.email = self.cleaned_data.get('email')
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
        new_user = User(username=self.username, email=self.email, password=make_password(self.password))
        if commit:
            new_user.save()
        return new_user
