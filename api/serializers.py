from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers
from dataview.models import *

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ('name', 'id')

    def create(self, validated_data):
        return Collections.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance



class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = '__all__'

    def get_field_map(self, obj):
        if not hasattr(self, "field_map"):
            fields = obj.collection.fields()
            # TODO: This assumes that there's only a single collection in this set
            self.field_map = {f.field_key: f.field_name for f in fields}
        return self.field_map
        
    def to_representation(self, obj):
        field_map = self.get_field_map(obj)
        return {field_map[key]: value for key, value in obj.row.items() if key in field_map}


