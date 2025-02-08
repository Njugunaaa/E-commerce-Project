from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)