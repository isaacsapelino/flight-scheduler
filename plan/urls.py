from django.urls import path
from . import views

urlpatterns = [
    path('', views.plan, name='plan'),
    path('addflights', views.addflights, name='addflights'),
]