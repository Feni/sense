from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import *

def home(request):
    return render(request, "index.html")