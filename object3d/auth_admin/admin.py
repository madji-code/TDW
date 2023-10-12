from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'lname', 'fname')
    list_filter = ('email', 'lname', 'fname', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'lname', 'fname', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'lname', 'fname',)}),
        ('Permission', {'fields': ('is_staff', 'is_active')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'lname', 'fname', 'password1', 'password2', 'is_staff', 'is_active',)
            }),
    )



admin.site.register(User, UserAdminConfig)
