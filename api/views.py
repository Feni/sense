from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CollectionRowsViewSet(viewsets.ModelViewSet):
    queryset = CollectionRows.objects.all()
    serializer_class = CollectionRowsSerializer