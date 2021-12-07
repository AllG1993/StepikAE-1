from django.shortcuts import render
from django.http import HttpResponse


def leo(requests):
    return HttpResponse('Знак зодиака - Лев')


def scorpio(requests):
    return HttpResponse('Знак зодиака - Скорпион')


def aries(requests):
    return HttpResponse('Знак зодиака - Овен')


def taurus(requests):
    return HttpResponse('Знак зодиака - Телец')

