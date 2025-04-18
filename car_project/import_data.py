import pandas as pd
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_project.settings')
django.setup()

# IMPORT MODELS
from car_app.models import Car #, Image

# Read the Excel files
cars_df = pd.read_excel('car data.xlsx')
#images_df = pd.read_excel('images.xlsx')

# Add data to Car model
for index, row in cars_df.iterrows():
    print(index)
    car, created = Car.objects.get_or_create(
        car_id=row['car_id'],
        defaults={
            'date': row['date'],
            'registrering': row['registrering'],
            'brand': row['brand'],            
            'model': row['model'],
            'fuel_type': row['fuel_type'],            
            'horsepower': row['horsepower'],
            'engine_size': row['engine_size'],
            'transimision': row['transimision'],
            'kilometer': row['kilometer'],
            'number_of_doors': row['number_of_doors'],
            'number_of_seats': row['number_of_seats'],
            'karosseri': row['karosseri'],
            'koretype': row['koretype'],
            'kosmetisk': row['kosmetisk'],
            'mekanisk': row['mekanisk'],
            'kommentar': row['kommentar'],
            'registeringsafgift': row['registeringsafgift'],
            'tax_moms_or_inkl': row['tax_moms_or_inkl'],
            'stelnummer': row['stelnummer'],
            'price': row['price'],
            'unique_identifier': row['unique_identifier'],
            'color': row['color'],
            'image_names': row['image_names'],
            'image_url_1': row['image_url_1'],
            'image_url_2': row['image_url_2'],
            'image_url_3': row['image_url_3'],
            'image_url_4': row['image_url_4'],
            'image_url_5': row['image_url_5']
        }
    )

 # Add data to Image model
#for index, row in images_df.iterrows():
#    car = Car.objects.get(car_id=row['car_id'])
#    Image.objects.get_or_create(
#        car=car,
#        image_path=row['image_path']
#    )

print("Data imported successfully!")