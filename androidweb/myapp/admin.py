from django.contrib import admin
from .models import Blog, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
