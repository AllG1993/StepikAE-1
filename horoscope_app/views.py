from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

import datetime


sh = {"aries": "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля)",
      "taurus": "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая)",
      "gemini": "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня)",
      "cancer": "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля)",
      "leo": "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа)",
      "virgo": "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября)",
      "libra": "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября)",
      "scorpio": "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября)",
      "sagittarius": "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря)",
      "capricorn": "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января",
      "aquarius": "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля)",
      "pisces": "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)"
      }

sign_types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}


def index(request):
    sh_key_list = list(sh)
    result = ''
    for sign in sh_key_list:
        sign_url = reverse('horoscope_name', args=[sign])
        result += f'<li><a href="{sign_url}">{sign.title()}</a></li>'
    return HttpResponse(f'<ol>{result}</ol>')


def sign_type_list(request):
    result = ''
    for element in list(sign_types_dict):
        url = reverse('sign_type_page', args=[element])
        result += f'<a href="{url}"><li>{element.title()}</li></a>'
    return HttpResponse(f'<ul>{result}</ul>')


def sign_type_page(request, sign_type):
    result = 'Нет такой стихии.'
    if sign_type in sign_types_dict:
        result = ''
        for st in sign_types_dict[sign_type]:
            sign_url = reverse('horoscope_name', args=[st])
            result += f'<a href="{sign_url}"><li>{st.title()} ({sh[st].split()[0]})</a></li>'
    return HttpResponse(f'<ul>{result}</ul>')


def get_info_sign_horoscope(requests, sign_horoscope: str):
    if sign_horoscope.lower() in sh:
        return HttpResponse(f'<h2>Знак зодиака: {sh[sign_horoscope]}</h2>')
    else:
        return HttpResponseNotFound(f'Знак зодиака: "{sign_horoscope}" не определен.')


def get_info_sign_horoscope_by_number(requests, sign_horoscope: int):
    sh_key_list = list(sh)
    if sign_horoscope > len(sh_key_list):
        return HttpResponseNotFound(f'Знак зодиака c номером: "{sign_horoscope}" отсутствует.')
    name_sh = sh_key_list[sign_horoscope - 1]
    redirect_url = reverse('horoscope_name', args=(name_sh,))
    return HttpResponseRedirect(redirect_url)


def determining_horoscope_sign(request, day: int, mo: int):
    result = HttpResponseNotFound('Некорректная дата.')
    if mo > 12 or day > 31:
        return result
    else:
        if (day >= 21 and mo == 3) or (day <= 20 and mo == 4):
            result = 'aries'
        elif (day >= 21 and mo == 4) or (day <= 21 and mo == 5):
            result = 'taurus'
        elif (day >= 22 and mo == 5) or (day <= 21 and mo == 6):
            result = 'gemini'
        elif (day >= 22 and mo == 6) or (day <= 22 and mo == 7):
            result = 'cancer'
        elif (day >= 23 and mo == 7) or (day <= 23 and mo == 8):
            result = 'leo'
        elif (day >= 24 and mo == 8) or (day <= 23 and mo == 9):
            result = 'virgo'
        elif (day >= 24 and mo == 9) or (day <= 23 and mo == 10):
            result = 'libra'
        elif (day >= 24 and mo == 10) or (day <= 22 and mo == 11):
            result = 'scorpio'
        elif (day >= 23 and mo == 11) or (day <= 21 and mo == 12):
            result = 'sagittarius'
        elif (day >= 22 and mo == 12) or (day <= 20 and mo == 1):
            result = 'capricorn'
        elif (day >= 21 and mo == 1) or (day <= 18 and mo == 2):
            result = 'aquarius'
        elif (day >= 19 and mo == 2) or (day <= 20 and mo == 3):
            result = 'pisces'

        url_sign = reverse('horoscope_name', args=[result])

        return HttpResponse(f'День: {day} Месяц: {mo} соответствует знаку - '
                            f'<a href="{url_sign}">{sh[result].split()[0]}</a>')


