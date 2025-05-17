from django.contrib import admin
from .models import Car     #, Image
# Register your models here.

admin.site.site_header = 'Car Management Admin'
admin.site.site_title = 'Car Admin Portal'
admin.site.index_title = 'Welcome to Car Management Dashboard'

class CarAdmin(admin.ModelAdmin):
    # list_display = ('car_id','date','make','model','year','price')
    # list_filter = ('date','make','model','year')
    # search_fields = ('date','make','model','year')
    # list_display = ('car_id','date','Registrering','brand','model','Fuel_Type')
    
    list_display = ('car_id','date','registrering','brand','model','fuel_type', 'horsepower', 'engine_size', 'transimision', 
                    'kilometer', 'number_of_doors', 'number_of_seats', 'karosseri', 'koretype', 'kosmetisk', 'mekanisk', 'kommentar', 
                    'registeringsafgift', 'tax_moms_or_inkl', 'stelnummer', 'price', 'unique_identifier', 'image_names', 
                    'image_url_1', 'image_url_2', 'image_url_3', 'image_url_4', 'image_url_5')
    
    list_filter = ('date','brand','model')
    search_fields = ('date','brand','model')


# Customizing column headers for existing fields
    def car_id_upper(self, obj):
        return obj.car_id
    car_id_upper.short_description = 'Car ID' # Custom column name in uppercase


admin.site.register(Car, CarAdmin)