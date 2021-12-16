from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('type', views.sign_type_list, name='type'),
    path('type/<str:sign_type>', views.sign_type_page, name='sign_type_page'),
    path('<int:sign_horoscope>', views.get_info_sign_horoscope_by_number),
    path('<str:sign_horoscope>', views.get_info_sign_horoscope, name='horoscope_name'),
    path('<int:day>/<int:mo>', views.determining_horoscope_sign, name='determining_horoscope_sign'),

]

