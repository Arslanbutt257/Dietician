from django.apps import AppConfig
from django.conf import settings
import os

import pandas as pd


class DeiticianConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Deitician'
    food = os.path.join(settings.BASE_DIR, 'Deitician/Datasets/food.csv')
    nutrition = os.path.join(settings.BASE_DIR, 'Deitician/Datasets/nutrition_distribution.csv')

    data = pd.read_csv(food)
    datafin = pd.read_csv(nutrition)
