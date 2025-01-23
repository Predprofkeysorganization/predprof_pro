from django.contrib import admin
from user.models import Inventory, Plan, Application, ApplicationRepair


admin.site.site_header = 'Панель администратора'


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'product_status')
    search_fields = ('name',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'provider')
    search_fields = ('name',)


@admin.register(Application)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id_application', 'name_application', 'status_application')
    search_fields = ('status_application',)


@admin.register(ApplicationRepair)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id_application_repair', 'name', 'repair_info', 'status_application')
    search_fields = ('id_application_repair', )
