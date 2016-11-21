from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.shortcuts import *
from .models import *
from .forms import *

def home(request):
    return render(request, "index.html")

class CollectionEntry(FormView):
    template_name = "dataview/collectionentry_form.html"

    def get_fields(self):
        json_fields = list(Collections.objects.get(id=1).fields().values_list("field_name", flat=True))
        return json_fields

    def get_form(self, form_class=None):
        return CollectionEntryForm(**self.get_form_kwargs(), json_fields=self.get_fields())

    def form_valid(self, form):
        fields = self.get_fields()
        values = {}
        for field in form.fields:
            if field.startswith("json_"):
                field_id = int(field.replace("json_", ""))
                field_name = fields[field_id]
                values[field_name] = form.cleaned_data[field]
        collection = Collections.objects.get(id=1)
        max_row_id = CollectionRows.max_id(collection)
        newrow = CollectionRows(row_id=max_row_id + 1, row=values, collection=collection)
        newrow.save()
        return redirect("/")
