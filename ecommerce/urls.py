from django.urls import path
from . import views as ecommerce_views

urlpatterns = [
    path('', ecommerce_views.home, name='home'),
    path('tickets/', ecommerce_views.tickets, name='tickets')
]
