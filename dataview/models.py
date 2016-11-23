from django.db.models import *
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Collections(Model):
    name = CharField(max_length=64)
    # Owners, users, etc. in a linked table

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # TODO: Some kind of non enumerable list later
        return "/collections/%d" % (self.id)

    def fields(self):
        return self.schemas_set.all()

class Schemas(Model):
    collection = ForeignKey("Collections")
    field_name = CharField(max_length=32, db_index=True)
    field_key = CharField(max_length=64, db_index=True)
    # type, order
    def __str__(self):
        return self.field_name

class Dataset(Model):
    collection = ForeignKey("Collections")
    row_id  = IntegerField(db_index=True)  # key
    row = JSONField(null=True)  # data
    
    @staticmethod
    def max_id(collection):
        return Dataset.objects.filter(collection=collection).aggregate(Max('row_id'))["row_id__max"]

    class Meta:
        unique_together = ("collection", "row_id")