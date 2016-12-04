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
            self._dataset = Dataset.objects.filter(collection=self.kwargs["collection_id"])
            if 'row_id' in self.kwargs:
                print(self.kwargs['row_id'])
                print(self._dataset)
                self._dataset = self._dataset.filter(row_id=int(self.kwargs['row_id'])).first()
        return self._dataset

    def get_context_data(self, **kwargs):
        context = super(DatasetContext, self).get_context_data(**kwargs)
        context["collection"] = self.get_collection()
        return context

class CollectionListView(ListView):
    model = Collections

class CollectionDetailView(CollectionsListContext, CollectionContext, DetailView):
    model = Collections
    pk_url_kwarg = 'collection_id'

class CollectionEntry(CollectionsListContext, CollectionContext, FormView):
    template_name = "dataview/collectionentry_form.html"

    def get_fields(self):
        json_fields = list(self.get_collection().fields().values_list("field_name", flat=True))
        return json_fields

    def get_form(self, form_class=None):
        return CollectionEntryForm(**self.get_form_kwargs(), json_fields=self.get_fields())

    def form_to_json(self, form):
        fields = self.get_fields()
        values = {}
        for field in form.fields:
            if field.startswith("json_"):
                field_id = int(field.replace("json_", ""))
                field_name = fields[field_id]
                values[field_name] = form.cleaned_data[field]
        return values

    def form_valid(self, form):
        json_form = self.form_to_json(form)
        collection = self.get_collection()
        max_row_id = Dataset.max_id(collection)
        newrow = Dataset(row_id=max_row_id + 1, row=json_form, collection=collection)
        newrow.save()
        return redirect("/")


class DataEntry(CollectionEntry, DatasetContext):
    def get_object(self):
        return self.get_dataset()

    def form_valid(self, form):
        json_form = self.form_to_json(form)
        obj = self.get_object()
        obj.row = {**dict(obj.row), **json_form}
        obj.save()
        return redirect("/")

    def get_initial(self):
        initial = super(DataEntry, self).get_initial()
        fields = self.get_collection().fields()
        entry = self.get_dataset()
        for i, field in enumerate(fields):
            initial['json_%s' % i] = entry.row[field.field_key]
        return initial
        

