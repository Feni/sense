from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *

# Create your views here.
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class CollectionsViewSet(viewsets.ModelViewSet):
    queryset = Collections.objects.all()
    serializer_class = CollectionSerializer

class CollectionDatasetViewSet(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer

    def get_queryset(self):
        c = Collections.objects.get(id=self.kwargs['collection_id'])
        return c.dataset_set.all()

class DatasetRowViewSet(viewsets.ModelViewSet):
    serializer_class = DatasetSerializer

    def get_queryset(self):
        c = Collections.objects.get(id=self.kwargs['collection_id'])
        return c.dataset_set.filter(row_id=self.kwargs['row_id'])