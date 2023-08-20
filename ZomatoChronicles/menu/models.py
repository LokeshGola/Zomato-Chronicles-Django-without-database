from django.db import models

# # Create your models here.

class Dish:
    def __init__(self, dish_name, price, availability=True):
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

    def __str__(self):
        return self.dish_name


# from django.db import models

# class Dish(models.Model):
#     dish_name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     availability = models.BooleanField(default=True)

#     def __str__(self):
#         return self.dish_name
#     class Meta:
#         app_label = 'menu'  # Replace with your app's name

# menu/models.py
# from django.db import models

# class MenuItem(models.Model):
#     dish_name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     availability = models.BooleanField(default=True)

#     def __str__(self):
#         return self.dish_name
#     class Meta:
#         app_label = 'menu'  # Replace with your app's name
