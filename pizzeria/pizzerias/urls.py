"""Defines URL patterns for pizzerias"""
from django.urls import path
from . import views

app_name='pizzerias'
urlpatterns=[
    #Home page
    path('',views.index, name='index'),
    # Page that shows all pizzas
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]
