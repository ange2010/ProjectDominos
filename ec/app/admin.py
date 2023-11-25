from django.contrib import admin
from .models import Product, Customer, Cart, Payment, OrderPlaced


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'category', 'product_image']
    list_display_links = ['id', 'title']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'locality', 'city', 'state', 'zipcode']
    list_display_links = ['id', 'name']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'product', 'quantity', 'ordered_date', 'status', 'payment']
    list_display_links = ['id', 'customer', 'product', 'ordered_date']
    ordering = ['-ordered_date']
    search_fields = ['user__username', 'status']
    list_filter = ['user__username', 'status']
