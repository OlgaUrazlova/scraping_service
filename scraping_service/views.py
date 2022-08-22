import datetime as datetime
from django.shortcuts import render


def home(request):
    date = datetime.datetime.now()
    name = 'Test User'
    sample_context = {
        'date': date,
        'name': name,
    }

    return render(request, 'home.html', sample_context)
