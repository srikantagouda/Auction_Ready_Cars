from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    #path('', login_required(views.car_list), name='car_list'),
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', login_required(views.car_detail), name='car_detail'),
]
