from django.forms import *

class CollectionEntryForm(Form):
    def __init__(self, *args, **kwargs):
        json_fields = kwargs.pop('json_fields')
        super(CollectionEntryForm, self).__init__(*args, **kwargs)

        for i, field in enumerate(json_fields):
            self.fields['json_%s' % i] = CharField(label=field)