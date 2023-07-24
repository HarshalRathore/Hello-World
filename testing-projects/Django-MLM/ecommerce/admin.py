from django.contrib import admin
from .models import Product, Category, Customer, Order, OrderItem, Shop, Cart, CartItem, BusinessVolumeLog
from import_export.admin import ImportExportModelAdmin
# Register your models here.

def copy_items(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()


copy_items.short_description = 'Copy Items'

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active'
    ]
    list_filter = ['title', 'is_active']
    search_fields = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}

class ProductAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'category',
        'in_stock',
    ]
    list_filter = ['category__title', 'in_stock']
    search_fields = ['name', 'category__title']
    actions = [copy_items]

class OrderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = [
        'customer',
        'status',
        'created_at'
    ]


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Shop)
admin.site.register(BusinessVolumeLog)