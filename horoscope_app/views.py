from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

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


def get_info_sign_horoscope(requests, sign_horoscope: str):
    if sign_horoscope.lower() in sh:
        return HttpResponse(f'Знак зодиака: {sh[sign_horoscope]}')
    else:
        return HttpResponseNotFound(f'Знак зодиака: "{sign_horoscope}" не определен.')


def get_info_sign_horoscope_by_number(requests, sign_horoscope: int):
    sh_key_list = list(sh)
    if sign_horoscope > len(sh_key_list):
        return HttpResponseNotFound(f'Знак зодиака c номером: "{sign_horoscope}" отсутствует.')
    name_sh = sh_key_list[sign_horoscope - 1]
    return HttpResponseRedirect(f'/horoscope/{name_sh}')


