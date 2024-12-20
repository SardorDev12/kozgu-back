from .models import User
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name']


admin.site.register(User, UserAdmin)