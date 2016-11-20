from django.db.models import *
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Collections(Model):
    name = CharField(max_length=64)
    # Owners, users, etc. in a linked table

    def __str__(self):
        return self.name

class CollectionFields(Model):
    collection = ForeignKey("Collections")
    field_name = CharField(max_length=32, db_index=True)
    field_key = CharField(max_length=64, db_index=True)
    # type, order
    def __str__(self):
        return self.field_name

class CollectionRows(Model):
    collection = ForeignKey("Collections")
    row_id  = IntegerField(db_index=True)
    row = JSONField(null=True)
    
    class Meta:
        unique_together = ("collection", "row_id")