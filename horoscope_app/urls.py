from django.urls import path
from . import views

urlpatterns = [
    path('<sign_horoscope>/', views.get_info_sign_horoscope),
    # path('leo/', views.leo),
    # path('scorpio/', views.scorpio),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
]
