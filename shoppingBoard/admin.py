from django.contrib import admin
from .models import Category,SubCategory,Inventory,productSpec ,Orders,OrderItems , UserData


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'gender')

class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('sub_category_name','current_gender')

class InventoryAdmin(admin.ModelAdmin):
    list_display=('name','unit_price','brand','get_photo')

class productSpecAdmin(admin.ModelAdmin):
    list_display=('productName','quantity','color','size')

class OrderAdmin(admin.ModelAdmin):
    list_display=('customer','paid')

class OrderItemsAdmin(admin.ModelAdmin):
    list_display=('product','ship_date','quantity','price','size','get_photo')
    list_filter = ['order']
admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Inventory,InventoryAdmin)
admin.site.register(productSpec,productSpecAdmin)
admin.site.register(Orders,OrderAdmin)
admin.site.register(OrderItems)
admin.site.register(UserData)
# Register your models here.
