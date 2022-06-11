from django.contrib import admin
from import_export.admin import ImportExportModelAdmin   # for import or export data in all types of files, such as csv, xls, json e.g

from .models import *
# Register your models here.

#registred with its featuded
class CarsAdmin(ImportExportModelAdmin, admin.ModelAdmin): 
    list_display = ('number', 'marck', 'model', 'color', 'date')
    search_fields = ('number', 'marck', 'model')
    readonly_fields = ()
    ordering = ['number']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    class Meta:
       model = Cars
    
admin.site.register(Cars, CarsAdmin)


class PersonsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('selfid', 'name', 'lastname', 'father', 'birth')
    search_fields = ('selfid', 'name', 'lastname','car')
    readonly_fields = ()
    ordering = ['selfid']
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    class Meta:
       model = Person

admin.site.register(Person, PersonsAdmin)



# class CarDriverAdmin(admin.ModelAdmin):
#     list_display = ('person',)
#     search_fields = ('person', 'car')
#     readonly_fields = ()
#     ordering = ['id']
#     filter_horizontal = ()
#     list_filter = ()
#     fieldsets = ()

# admin.site.register(CarDriver, CarDriverAdmin)

# class VideoAdminModel(admin.ModelAdmin):
#     search_fields=['name'+'lastname','selfid', 'number', 'model', 'marck']

# admin.site.register(VideoAdminModel)