from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render

def equipments(request):
    return render(request, 'equipments.html')