from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from .models import Car  # , Image

def car_list(request):

    #Get Selected Filters.
    selected_brands = request.GET.getlist('carbrands')

    #return HttpResponse(selected_brands)
    selected_models = request.GET.getlist('carmodels')
    selected_fuel_types = request.GET.getlist('carfueltypes')

    cars = Car.objects.all()
    
    if selected_brands:
        cars = cars.filter(brand__in=selected_brands)
    if selected_models:
        cars = cars.filter(model__in=selected_models)
    if selected_fuel_types:
        cars = cars.filter(fuel_type__in=selected_fuel_types)

    #Get Unique items for the filter select.
    brand_column = Car.objects.values_list('brand', flat=True).distinct()
    model_column = Car.objects.values_list('model', flat=True).distinct()
    fuel_type_column = Car.objects.values_list('fuel_type', flat=True).distinct()

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
        'cars': cars,
        'page_obj': page_obj,
        'brand_column' : brand_column,
        'model_column' : model_column,
        'fuel_type_column' : fuel_type_column,
        'selected_brands' : selected_brands,
        'selected_models' : selected_models,
        'selected_fuel_types' : selected_fuel_types,

        'get_params' : get_params.urlencode()
    })

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    images = car.image_names.split(',')
    # images = Image.objects.filter(car=car)
    return render(request, 'car_app/car_detail.html', {'car': car, 'images': images})