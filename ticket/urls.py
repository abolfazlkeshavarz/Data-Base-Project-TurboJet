from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('flights/', views.flights, name='flights'),
    path('buy/', views.buy, name='buy_ticket'),
    path('why-TurboJet/', views.whyus, name='whyus'),
    path('about-us/', views.about, name='about')
]
