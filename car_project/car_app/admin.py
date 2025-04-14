from django.contrib import admin
from .models import Car     #, Image
# Register your models here.

admin.site.site_header = 'Car Management Admin'
admin.site.site_title = 'Car Admin Portal'
admin.site.index_title = 'Welcome to Car Management Dashboard'

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id','date','make','model','year','price')

    list_filter = ('date','make','model','year')

    search_fields = ('date','make','model','year')

admin.site.register(Car,CarAdmin)