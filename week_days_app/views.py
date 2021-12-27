from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

wd = {
    'monday': 'понедельник',
    'tuesday': 'вторник',
    'wednesday': 'среда',
    'thursday': 'четверг',
    'friday': 'пятница',
    'saturday': 'суббота',
    'sunday': 'воскресенье',
}

wd_list = [
    'понедельник',
    'вторник',
    'среда',
    'четверг',
    'пятница',
    'суббота',
    'воскресенье',
]


def get_week_day(requests, week_day: str):
    if week_day in wd:
        return HttpResponse(f'Список дел, на {wd[week_day]}.')
    else:
        return HttpResponseNotFound(f'Нет дня недели: {week_day}.')


def get_week_day_by_number(requests, week_day: int):
    key_list = list(wd)
    week_day -= 1
    if abs(week_day) < 7:
        redirect_url = reverse('week_day_page', args=(key_list[week_day],))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Нет дня недели под номером: {week_day + 1}.')



