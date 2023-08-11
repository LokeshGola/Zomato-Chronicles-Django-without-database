from django.db import models

# Create your models here.

class Dish:
    def __init__(self, dish_name, price, availability=True):
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def __str__(self):
        return self.dish_name


