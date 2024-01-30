from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Aircraft)
admin.site.register(models.Airline)
admin.site.register(models.Airport)
admin.site.register(models.FlightInfo)
admin.site.register(models.Ticket)
admin.site.register(models.Payment)
