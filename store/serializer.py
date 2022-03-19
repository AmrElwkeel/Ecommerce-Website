from rest_framework import serializers
from rest_framework.serializers import Serializer

from store.models import Product

class storeSerializers(serializers.ModelSerializer):
     class Meta:
          model = Product
          fields = '__all__'

