from django.db import models

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)

    date = models.DateField()    
    registrering = models.DateField()   

    brand = models.CharField(max_length=255, null=True, blank=True)    
    model = models.CharField(max_length=255, null=True, blank=True)
    fuel_type = models.CharField(max_length=255, null=True, blank=True)    
    
    horsepower = models.IntegerField(null=True, blank=True)
    engine_size = models.IntegerField(null=True, blank=True)

    transimision = models.CharField(max_length=255, null=True, blank=True)

    kilometer = models.IntegerField(null=True, blank=True)
    number_of_doors = models.IntegerField(null=True, blank=True)
    number_of_seats = models.IntegerField(null=True, blank=True)

    karosseri = models.CharField(max_length=255, null=True, blank=True)
    koretype = models.CharField(max_length=255, null=True, blank=True)

    kosmetisk = models.IntegerField(null=True, blank=True)

    mekanisk = models.CharField(max_length=255, null=True, blank=True)
    
    kommentar = models.TextField(null=True, blank=True)

    registeringsafgift = models.CharField(max_length=255, null=True, blank=True)
    tax_moms_or_inkl = models.CharField(max_length=255, null=True, blank=True)
    stelnummer = models.CharField(max_length=255, null=True, blank=True)

    price = models.IntegerField(null=True, blank=True)

    unique_identifier = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=255, null=True, blank=True)

    image_names = models.TextField(max_length=2000, default='notavailable.jpg')            #Comma Separated Image Names with Ext
    
    image_url_1 = models.CharField(max_length=255, null=True, blank=True)
    image_url_2 = models.CharField(max_length=255, null=True, blank=True)
    image_url_3 = models.CharField(max_length=255, null=True, blank=True)
    image_url_4 = models.CharField(max_length=255, null=True, blank=True)
    image_url_5 = models.CharField(max_length=255, null=True, blank=True)

    # Add other car details as needed

#class Image(models.Model):
#    car = models.ForeignKey(Car, on_delete=models.CASCADE)
#    image_path = models.CharField(max_length=255)

