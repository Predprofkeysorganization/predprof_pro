from django.contrib import admin
from user.models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'product_status')
    search_fields = ('name',)


admin.site.site_header = 'Панель администратора'
