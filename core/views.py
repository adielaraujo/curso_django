from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context = {'mensagem':'Ola mundo'}
    return render(request, 'core/index.html', context)


