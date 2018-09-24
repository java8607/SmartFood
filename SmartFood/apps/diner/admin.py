from django.contrib import admin

from apps.diner.models import Diner, HealthCharacteristic, Preference

# Register your models here.
admin.site.register(Diner)
admin.site.register(HealthCharacteristic)
admin.site.register(Preference)