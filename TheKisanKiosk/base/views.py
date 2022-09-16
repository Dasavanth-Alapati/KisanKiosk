from django.shortcuts import render
from .sessions import sessiondetails


def homepage(request):
    return render(request, 'home.html', sessiondetails(request))
