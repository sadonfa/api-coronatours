from rest_framework import serializers
from tours.models import Tours


class ToursSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tours
        fields = ['id', 'name', 'description', 'image1',
                  'image2', 'image3', 'image4', 'info', 'include', 'noinclude', 'cash']
