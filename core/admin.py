from django.contrib import admin
from .models import Category, Product, Order, Cart  # ✅ Added Cart

# ✅ Category Admin
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug from name
    list_display = ('name',)  # Display category names in the admin panel

# ✅ Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'available', 'seller')  # ✅ Added seller and availability
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'available')  # ✅ Filter by category and availability
    prepopulated_fields = {'slug': ('name',)}  # Auto-generate slug

# ✅ Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price', 'status', 'created_at')  # ✅ Added product & created_at
    list_filter = ('status', 'created_at')  # ✅ Added created_at filter
    search_fields = ('user__username', 'product__name')  # ✅ Search orders by user or product name

# ✅ Cart Admin
class CartAdmin(admin.ModelAdmin):  # ✅ Added Cart admin
    list_display = ('user', 'product', 'quantity')
    search_fields = ('user__username', 'product__name')

# ✅ Register Models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)  # ✅ Registered Cart
