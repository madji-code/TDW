from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):

    def create_superuser(self, fname, lname, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(fname, lname, email, password, **extra_fields)

    def create_user(self, fname, lname, email, password, **extra_fields):
        if not email:
            raise ValueError(_("You have not provided a valid e-mail address!"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, fname=fname, lname=lname, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    fname = models.CharField(_('First name'), max_length=30)
    lname = models.CharField(_('Last name'), max_length=30)
    rpassword = models.CharField("Entrez à nouveau votre mot de passe", max_length=150, null = True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['fname', 'lname']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    # def get_full_name(self):
    #     return self.firtname + self.lastname
    
    # def get_short_name(self):
    #     return self.firtname
    
    def __str__(self):
        return f"\nUser ({self.id}) <email: {self.email}, is_active?: {self.is_active}>\n"