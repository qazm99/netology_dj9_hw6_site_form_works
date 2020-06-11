from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    amount_sum = None
    form = CalcForm(request.GET or None)
    if form.is_valid():
        initial_fee = form.cleaned_data.get('initial_fee')
        rate = form.cleaned_data.get('rate')
        months_count = form.cleaned_data.get('months_count')
        # Х = (стоимость + стоимость * процентную ставку) / срок    в    месяцах.
        amount_sum = initial_fee + initial_fee * ((rate / 100) * (months_count / 12))
        per_mounth_sum = amount_sum / months_count
    context = {
        'form': form,

    }
    if amount_sum:
        context.update({'common_result': f"{amount_sum:.2f}", 'per_mounth_sum': f"{per_mounth_sum:.2f}"})

    return render(request, template, context)
