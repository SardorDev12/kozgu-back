# posts/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_author', 'status', 'created_at')  # Using the get_author method
    list_filter = ('status', 'created_at', 'author')  # Correct filter for the author foreign key
    search_fields = ('title', 'content')

    def get_author(self, obj):
        return obj.author.username  # Accessing the username of the related User object
    get_author.short_description = 'Author'  # Setting the header for the column
