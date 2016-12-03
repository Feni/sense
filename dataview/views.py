from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import FormView
from django.views.generic.base import ContextMixin
from django.views.generic import *
from django.shortcuts import *
from .models import *
from .forms import *


class CollectionsListContext(ContextMixin):
    def get_collections(self):
        return Collections.objects.all()[:10] # TODO: Limit to user

    def get_context_data(self, **kwargs):
        context = super(CollectionsListContext, self).get_context_data(**kwargs)
        context["collections_list"] = self.get_collections()
        return context

class CollectionContext(ContextMixin):
    def get_collection(self):
        if not hasattr(self, "_collection"):
            self._collection = Collections.objects.get(id=self.kwargs["collection_id"])
        return self._collection

    def get_context_data(self, **kwargs):
        context = super(CollectionContext, self).get_context_data(**kwargs)
        context["collection"] = self.get_collection()
        return context

class DatasetContext(ContextMixin):
    def get_dataset(self):
        if not hasattr(self, "_dataset"):
            self._dataset = Dataset.objects.get(id=self.kwargs["collection_id"])
        return self._dataset

    def get_context_data(self, **kwargs):
        context = super(CollectionContext, self).get_context_data(**kwargs)
        context["collection"] = self.get_collection()
        return context

class CollectionListView(ListView):
    model = Collections

class CollectionDetailView(CollectionsListContext, DetailView):
    model = Collections

class CollectionEntry(CollectionsListContext, CollectionContext, FormView):
    template_name = "dataview/collectionentry_form.html"

    def get_fields(self):
        json_fields = list(self.get_collection().fields().values_list("field_name", flat=True))
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
        collection = self.get_collection()
        max_row_id = Dataset.max_id(collection)
        newrow = Dataset(row_id=max_row_id + 1, row=values, collection=collection)
        newrow.save()
        return redirect("/")

