from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.



class CustomUserAdmin(UserAdmin):
      fieldsets = UserAdmin.fieldsets + (('Photo', {"fields": ["image"]}),
                                         ('Personal Info', {"fields": ['phone_number','tc','is_teacher','description','rozet','slug']}),)

admin.site.register(CustomUser, CustomUserAdmin)



admin.site.register(Rozetler)