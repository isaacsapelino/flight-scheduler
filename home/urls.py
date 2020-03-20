from django.urls import path, re_path
from . import views
from plan import views as plan_views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('flights/', views.flights, name='flights'),
    path('schedules/', views.schedules, name='schedules'),
    path('checkout/', views.checkout, name='checkout'),
    path('del_flights/<int:pk>/delete', views.del_flights, name='del_flights'),
    path('add_flight_plan/<int:pk>/add', plan_views.add_flight_plan, name='add_flight_plan'),
    path('del_flight_plan/<int:pk>/delete', plan_views.del_flight_plan, name='del_flight_plan'),
    path('details/<int:pk>', views.details, name='details'),
]
