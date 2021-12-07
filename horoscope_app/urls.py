from django.urls import path
from . import views

urlpatterns = [
    path('leo/', views.leo),
    path('scorpio/', views.scorpio),
    path('aries/', views.aries),
    path('taurus/', views.taurus),
]