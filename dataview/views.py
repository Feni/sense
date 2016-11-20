from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import *
from .models import *

def home(request):
    return render(request, "index.html")

def rows(request):
    # Get the default collection for now
    c = Collections.objects.get(id=1)
    fields = CollectionFields.objects.filter(collection=c)
    rows = CollectionRows.objects.filter(collection=c)
    data = []
    # Remap field keys to field names
    for row in rows:
        obj = {}
        for field in fields:
            if field.field_key in row.row:
                obj[field.field_name] = row.row[field.field_key]
        data.append(obj)

    return JsonResponse({"data": data})