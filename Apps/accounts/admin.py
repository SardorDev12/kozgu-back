from .models import User
from django.contrib import admin

class UserAdmin(admin.ModelAdmin):
    list_display = ['username']


admin.site.register(User, UserAdmin)