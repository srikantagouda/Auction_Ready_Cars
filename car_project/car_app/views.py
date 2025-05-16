import json

from datetime import datetime, date
from itertools import chain

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from .models import Car  # , Image

#@login_required
def car_list(request):
    
    #return HttpResponse(request)
    #Get Selected Filters.
    selected_brands = request.GET.getlist('carbrands')
    selected_models = request.GET.getlist('carmodels')
    selected_fuel_types = request.GET.getlist('carfueltypes')
    selected_transimisions = request.GET.getlist('cartransimisions')

    selected_registeringsafgift = request.GET.getlist('registeringsafgift')
    selected_filter_tax = request.GET.getlist('filter_tax')
    
    date_from = request.GET.get('filterby_datefrom')
    date_to = request.GET.get('filterby_dateto')
    
    # Convert the date strings to datetime objects
    if date_from:
        #date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
        try:
            date_from = date(int(date_from), 1, 1)
        except:
            date_from = None
    if date_to:
        #date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
        try:
            date_to = date(int(date_to), 12, 31)
        except:
            date_to = None

    selected_km_from = request.GET.get('filterby_kmfrom')
    selected_km_to = request.GET.get('filterby_kmto')

    if selected_km_from:
        try:
            selected_km_from = int(selected_km_from)
        except:
            selected_km_from = None
    if selected_km_to:
        try:
            selected_km_to = int(selected_km_to)
        except:
            selected_km_to = None
    
    #cars = Car.objects.all()
    
    #Prepare the filter Parameters.
    filter_params = {}

    if selected_brands:
        filter_params['brand__in'] = selected_brands
        #cars = cars.filter(brand__in=selected_brands)
    if selected_models:
        filter_params['model__in'] = selected_models
        #cars = cars.filter(model__in=selected_models)
    if selected_fuel_types:
        filter_params['fuel_type__in'] = selected_fuel_types
        #cars = cars.filter(fuel_type__in=selected_fuel_types)
    if selected_transimisions:
        filter_params['transimision__in'] = selected_transimisions
        #cars = cars.filter(transimision__in=selected_transimisions)

    if selected_registeringsafgift:
        filter_params['registeringsafgift__in'] = selected_registeringsafgift
        #cars = cars.filter(registeringsafgift__in=selected_registeringsafgift)
    if selected_filter_tax:
        filter_params['tax_moms_or_inkl__in'] = selected_filter_tax
        #cars = cars.filter(tax_moms_or_inkl__in=selected_filter_tax)


    if date_from and date_to:
        #cars = cars.filter(date__gte=date_from, date__lte=date_to)
        filter_params['registrering__range'] = (date_from, date_to)
        #filter_params['registrering__lte'] = date_to
        #cars = cars.filter(registrering__gte=date_from, registrering__lte=date_to)
    elif date_from:
        #cars = cars.filter(date__gte=date_from)
        filter_params['registrering__gte'] = date_from
        #cars = cars.filter(registrering__gte=date_from)
    elif date_to:
        #cars = cars.filter(date__lte=date_to)
        filter_params['registrering__lte'] = date_to
        #cars = cars.filter(registrering__lte=date_to)

    if selected_km_from and selected_km_to:
        filter_params['kilometer__range'] = (selected_km_from, selected_km_to)
        #cars = cars.filter(kilometer__gte=selected_km_from, kilometer__lte=selected_km_to)
    elif selected_km_from:
        filter_params['kilometer__gte'] = selected_km_from
        #cars = cars.filter(kilometer__gte=selected_km_from)
    elif selected_km_to:
        filter_params['kilometer__lte'] = selected_km_to
        #cars = cars.filter(kilometer__lte=selected_km_to)

    db1_cars = Car.objects.using('default').filter(**filter_params).order_by('-date','-car_id')
    db2_cars = Car.objects.using('db2').filter(**filter_params).order_by('-date','-car_id')

    #cars = list(db1_cars) + list(db2_cars)
    cars = sorted(
        chain(db1_cars, db2_cars),
        key=lambda car: (car.date, car.car_id),
        reverse=True
    )
    
    #Below is the method of db order_by
    #cars = cars.order_by('-date','car_id')
    
    # Assuming 'cccc' is the value you want to compare against
    #cars = cars.filter(other__in=selected_others, column_name__gte=cccc)


    #Get Unique items for the filter select.
    #brand_column = Car.objects.values_list('brand', flat=True).distinct().order_by('brand')
    #model_column = Car.objects.values_list('model', flat=True).distinct().order_by('model')
    #fuel_type_column = Car.objects.values_list('fuel_type', flat=True).distinct()
    registeringsafgift_column = Car.objects.values_list('registeringsafgift', flat=True).distinct()
    filter_tax_column = Car.objects.values_list('tax_moms_or_inkl', flat=True).distinct()

    car_data = list(Car.objects.values('brand', 'model', 'fuel_type','transimision').distinct().order_by('brand', 'model'))
    car_data_json = json.dumps(car_data)

    selected_brands = json.dumps(selected_brands)
    selected_models = json.dumps(selected_models)
    selected_fuel_types = json.dumps(selected_fuel_types)
    selected_transimisions = json.dumps(selected_transimisions)

    paginator = Paginator(cars, 100)
    page_number = request.GET.get('page')

    if page_number == None:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    #Preserve the Get parameters in Pagination.
    get_params = request.GET.copy()
    if 'page' in get_params:
        get_params.pop('page')

    return render(request, 'car_app/car_list.html',{
        # 'cars': cars,
        'page_obj': page_obj,
        #'brand_column' : brand_column,
        #'model_column' : model_column,
        #'fuel_type_column' : fuel_type_column,
        'selected_registeringsafgift' : selected_registeringsafgift,
        'registeringsafgift_column' : registeringsafgift_column,
        'selected_filter_tax' : selected_filter_tax,
        'filter_tax_column' : filter_tax_column,


        'selected_brands' : selected_brands,
        'selected_models' : selected_models,
        'selected_fuel_types' : selected_fuel_types,
        'selected_transimisions' : selected_transimisions,
        
        'car_data_json' : car_data_json,

        'selected_km_from' : request.GET.get('filterby_kmfrom',''),
        'selected_km_to' : request.GET.get('filterby_kmto',''),
        'selected_date_from': request.GET.get('filterby_datefrom',''),
        'selected_date_to':request.GET.get('filterby_dateto',''),

        'get_params' : get_params.urlencode()
    })

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    images = car.image_names.split(',')
    # images = Image.objects.filter(car=car)
    return render(request, 'car_app/car_detail.html', {'car': car, 'images': images})