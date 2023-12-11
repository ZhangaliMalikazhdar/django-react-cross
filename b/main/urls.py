# yourapp/urls.py
from django.urls import path
from django.views.generic import TemplateView

from .views import react_app

urlpatterns = [
    path('', TemplateView.as_view(template_name='build/index.html')),
    path('react/', react_app, name='react_app'),
]

