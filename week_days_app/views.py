from django.shortcuts import render
from django.http import HttpResponse


def monday(requests):
    return HttpResponse('Список дел, на понедельник.')


def tuesday(requests):
    return HttpResponse('Список дел, на вторник.')

