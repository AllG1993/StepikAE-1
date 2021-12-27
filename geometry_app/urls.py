from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rectangle/<int:width>/<int:height>', views.get_rectangle_area, name='rectangle'),
    path('square/<int:width>', views.get_square_area, name='square'),
    path('circle/<int:radius>', views.get_circle_area, name='circle'),
    path('<str:page>/<str:params>', views.redirect_page),
]

