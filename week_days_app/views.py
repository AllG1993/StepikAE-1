from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_week_day(requests, week_day):
    wd = {
        'monday': 'понедельник',
        'tuesday': 'вторник',
        'wednesday': 'среда',
        'thursday': 'четверг',
        'friday': 'пятница',
        'saturday': 'суббота',
        'sunday': 'воскресенье',
    }
    if week_day in wd:
        return HttpResponse(f'Список дел, на {wd[week_day]}.')
    else:
        return HttpResponseNotFound(f'Нет дня недели: {week_day}.')


