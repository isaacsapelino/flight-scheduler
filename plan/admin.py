from django.contrib import admin
from .models import Flights, Booker, Planner, PlannedFlights
# Register your models here.
admin.site.register(Flights)
admin.site.register(Booker)
admin.site.register(Planner)
admin.site.register(PlannedFlights)
