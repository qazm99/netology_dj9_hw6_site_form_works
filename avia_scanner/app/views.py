from django.shortcuts import render
from django.http import JsonResponse
from django.core.cache import cache

from .models import City
from .forms import SearchTicket


def ticket_page_view(request):
    template = 'app/ticket_page.html'

    context = {
        'form': SearchTicket()
    }

    return render(request, template, context)


def cities_lookup(request):
    """Ajax request предлагающий города для автоподстановки, возвращает JSON"""
    city_str = request.GET.get('term')
    if cache.get('cities'):
        cities_list = cache.get('cities')
    else:
        cities_list = list(map(lambda city: city[0], City.objects.all().values_list('name')))
        cache.set('cities', cities_list, 300)
    cities_list_filter = []
    stri = 'sty'
    stri.lower()
    for city in cities_list:
        if city.lower().find(city_str.lower()) >= 0:
            cities_list_filter.append(city)

    return JsonResponse(cities_list_filter, safe=False)
