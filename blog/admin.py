from django.contrib import admin
from .models import  BlogArticles
# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title','author']}),
        ('Date information', {'fields': ['publish'], 'classes': ['collapse']}),
        ('Article_Body',     {'fields': ['body']}),
    ]
    list_display = ['title','publish','colored_status']
    list_filter = ['publish','author']
    search_fields = ['title','body']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)
