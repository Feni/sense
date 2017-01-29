from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import ContextMixin
from django.views.generic import *
from django.shortcuts import *
from .models import *

from django.shortcuts import render

# Create your views here.

class LingoHome(TemplateView):
    template_name = "lingo.html"