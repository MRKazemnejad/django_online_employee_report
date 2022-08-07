from django.contrib import admin
from .models import Product,Category,Order,OrderItem,Coupon

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','available',)
    prepopulated_fields={'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug':('name',)}



class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemInline,)
    list_display = ('user','updated','paid',)

admin.site.register(Coupon)



