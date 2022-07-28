from django.contrib import admin
from .models import Product,Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','available',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}







