from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.



class ProfileInstanceInline(admin.StackedInline):
    model=Profile
    can_delete= False
    verbose_name_plural= 'Profiles'
    extra=1



class CustomUserAdmin (UserAdmin):
    inlines=(ProfileInstanceInline,)
    search_help_text=('Buscar por: usuario, email')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)