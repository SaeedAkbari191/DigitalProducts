from django.contrib import admin

from products.models import Product, Category,File


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enabled','created_at']
    list_filter = ['is_enabled','created_at']
    search_fields = ['title']

class FileInlineAdmin(admin.StackedInline):
    model=File
    fields = ['file','title','is_enabled']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_enabled', 'created_at']
    list_filter = ['is_enabled']
    search_fields = ['title']
    inlines = [FileInlineAdmin]
