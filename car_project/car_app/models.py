from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    date = models.DateField()
    brand = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine_size = models.IntegerField()
    horsepower = models.IntegerField()
    price = models.IntegerField()
    year = models.IntegerField()

    image_names = models.TextField(max_length=2000, default='notavailable.jpg')            #Comma Separated Image Names with Ext

    # Add other car details as needed

# class Image(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     image_path = models.CharField(max_length=255)

