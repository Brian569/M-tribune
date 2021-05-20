from django.contrib import admin
from .models import Article , Tags,Profile

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'post', 'editor')
    filter_horizontal=('tags',)

@admin.register(Profile)
class EditorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username')
    

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)