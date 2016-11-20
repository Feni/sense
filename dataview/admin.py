from django.contrib import admin
import inspect
import sys
from .models import *


# Register your models here.
admin.site.register(Collections)

classes = inspect.getmembers(sys.modules['dataview.models'], lambda member: inspect.isclass(member) and member.__module__ == "dataview.models")
for class_name, clazz in classes:
    if clazz not in admin.site._registry:
        admin.site.register(clazz)