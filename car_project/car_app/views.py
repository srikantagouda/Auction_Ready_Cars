from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from .models import Car  # , Image

def car_list(request):
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    # Process the parameters as needed 

    make = request.GET.get('make')
    if make:
        cars = Car.objects.filter(make__icontains=make)
    else:
        cars = Car.objects.all()
    
    paginator = Paginator(cars, 20)
    page_number = request.GET.get('page')

    if page_number == None:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    return render(request, 'car_app/car_list.html', {'cars': cars, 'page_obj': page_obj})

def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    images = car.image_names.split(',')
    # images = Image.objects.filter(car=car)
    return render(request, 'car_app/car_detail.html', {'car': car, 'images': images})
