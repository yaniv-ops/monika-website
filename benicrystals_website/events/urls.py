from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, 
    name="home"),
    path('/contact_us', views.contact, 
    name="contact_us")
]