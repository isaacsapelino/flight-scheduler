from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage, name='loginPage'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.reg, name='reg'),
]