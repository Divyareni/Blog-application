from django.contrib import admin
from .models import Post, Comment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'content', 'published_date']
    list_display_links = ['post_title']
    list_filter = ['published_date']
    search_fields = ['post_title']

admin.site.register(Comment)

#admin.site.register(Post, PostAdmin)
