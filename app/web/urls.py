from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('breadboard', views.breadboard, name='breadboard'),
    path('cuttingboard', views.cuttingboard, name='cuttingboard'),
    path('pizzaboard', views.pizzaboard, name='pizzaboard'),
    path('faq', views.faq, name='faq'),
    path('terms', views.terms, name='terms')
]