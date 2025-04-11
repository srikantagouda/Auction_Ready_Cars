from django.shortcuts import render, HttpResponse
from .models import Car     #, Image

def car_list(request):
    param1 = request.GET.get('param1')
    param2 = request.GET.get('param2')
    # Process the parameters as needed 

    make = request.GET.get('make')
    if make:
        cars = Car.objects.filter(make__icontains=make)
    else:
        cars = Car.objects.all()
    
    context = { 
        'param1': param1,
        'param2': param2,
        'cars'  : cars,
    }

    return render(request, 'car_app/car_list.html', {'context': context})


def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)
    images = car.image_names.split()
    #images = Image.objects.filter(car=car)
    return render(request, 'car_app/car_detail.html', {'car': car, 'images': images})