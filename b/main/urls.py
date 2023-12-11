# yourapp/urls.py
from django.urls import path
from .views import react_app

urlpatterns = [
    path('react/', react_app, name='react_app'),
]

