from django.shortcuts import render,  redirect
from django.http import HttpResponse

# Create your views here.

def website_home(request):
    return render(request, 'website/index.html')