from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sign_horoscope>', views.get_info_sign_horoscope_by_number),
    path('<str:sign_horoscope>', views.get_info_sign_horoscope, name='horoscope_name'),
]
