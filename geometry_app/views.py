from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


def index(requests):
    return HttpResponse('<h1>Hello to geometry app</h1>')


def get_rectangle_area(requests, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника с шириной <strong>{width}</strong> и длинной '
                        f'<strong>{height}</strong> = <strong>{width * height}</strong>')


def get_square_area(requests, width):
    return HttpResponse(f'Площадь квадрата со стороной <strong>{width}</strong> = <strong>{width ** 2}</strong>')


def get_circle_area(requests, radius):
    return HttpResponse(f'Площадь круга с радиусом <strong>{radius}</strong> = <strong>{pi * (radius ** 2)}</strong>')


def redirect_page(requests, page, params):
    return HttpResponse(page, params)


