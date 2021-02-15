import random as r

from multiprocessing.reduction import register

from django.shortcuts import render

from django.http import JsonResponse
from django.template import loader


def index(request):
    context = {
        "num": rand()
    }
    return render(request, 'ran.html', context)


def ajax(request):
    data = {
        'num': rand()
    }
    return JsonResponse(data)


def rand():
    return r.randint(0,9999)
