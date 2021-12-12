from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_info_sign_horoscope(requests, sign_horoscope):
    sh = {
        'aries': 'Овен',
        'taurus': 'Телец',
        'twins': 'Близнецы',
        'crayfish': 'Рак',
        'leo': 'Лев',
        'virgo': 'Дева',
        'scales': 'Весы',
        'scorpion': 'Скорпион',
        'ophiuchus': 'Змееносец',
        'sagittarius': 'Стрелец',
        'capricorn': 'Козерог',
        'aquarius': 'Водолей',
    }
    if sign_horoscope.lower() in sh:
        return HttpResponse(f'Знак зодиака - {sh[sign_horoscope]}')
    else:
        return HttpResponseNotFound(f'Знак зодиака "{sign_horoscope}" не определен.')
