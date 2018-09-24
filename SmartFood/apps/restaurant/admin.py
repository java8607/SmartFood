from django.contrib import admin

from apps.restaurant.models import Ingredient, Product, Menu, Restaurant, Schedule, Manager

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Product)
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Schedule)
admin.site.register(Manager)