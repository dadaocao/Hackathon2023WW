from django.contrib import admin
from .models import Post


# add
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'date_created', 'author')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Post, PostAdmin)
