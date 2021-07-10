from django.urls import path
from .views import *

urlpatterns = [
    path('', main_page, name='main'),
    path('/contact/', contact, name='contact'),
    path('/about/', about, name='about'),
]