import pandas as pd
from car_app.models import Car  #, Image
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'car_project.settings')
django.setup()

# Read the Excel files
cars_df = pd.read_excel('cars.xlsx')
#images_df = pd.read_excel('images.xlsx')

# Add data to Car model
for index, row in cars_df.iterrows():
    car, created = Car.objects.get_or_create(
        car_id=row['car_id'],
        defaults={
            'make': row['make'],
            'model': row['model'],
            'year': row['year'],
            'engine_size': row['engine_size'],
            'horsepower': row['horsepower'],
            'price': row['price']
        }
    )

# # Add data to Image model
# for index, row in images_df.iterrows():
#     car = Car.objects.get(car_id=row['car_id'])
#     Image.objects.get_or_create(
#         car=car,
#         image_path=row['image_path']
#     )

print("Data imported successfully!")