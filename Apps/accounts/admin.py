from .models import CustomUser
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']

admin.site.register(CustomUser, UserAdmin)