from django import forms

from .widgets import AjaxInputWidget



class SearchTicket(forms.Form):

    attrs = {'class': 'inline right-margin', 'font-size': '12px'}
    city_start = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs), label='Город отправления ')

    city_end = forms.CharField(widget=AjaxInputWidget('api/city_ajax', attrs), label='Город прибытия ')
    date_fly = forms.DateField(widget=forms.SelectDateWidget, label='Дата вылета')

