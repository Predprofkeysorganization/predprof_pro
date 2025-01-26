from django.contrib import admin
from user.models import Inventory, Plan, Application, ApplicationRepair, Report


admin.site.site_header = 'Панель администратора'


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'count', 'product_status')
    search_fields = ('name',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'provider')
    search_fields = ('name',)


@admin.register(Application)
class AppAdmin(admin.ModelAdmin):
    list_display = ('id_application', 'name_application', 'status_application', 'information')
    search_fields = ('status_application',)


@admin.register(ApplicationRepair)
class AppAdminRepair(admin.ModelAdmin):
    list_display = ('id_application_repair', 'name', 'repair_info', 'status_application')
    search_fields = ('id_application_repair', )


@admin.register(Report)
class AdminReport(admin.ModelAdmin):
    list_display = ('id_report', 'name_manager', 'status_report')
    search_fields = ('name_manager',)