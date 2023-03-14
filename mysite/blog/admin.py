from django.contrib import admin
from .models import Post
# Register your models here.

# Customize the admin interface for the 'Post' model by specifying which fields to display, how to filter and search instances,
# and how to handle certain fields like 'slug' and 'author'
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'

