from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import request

def welcome(request):
    return render(request, 'show.html')
