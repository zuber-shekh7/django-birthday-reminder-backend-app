from rest_framework import serializers

from .models import Birthday


class CreateBirthdaySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    image = serializers.ImageField(required=True)
    
    class Meta:
        model = Birthday
        fields = ('name', 'birth_date', 'image')


class BirthdaySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    birth_date = serializers.DateField(required=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    
    class Meta:
        model = Birthday
        fields = ('id', 'name', 'birth_date', 'image_url')

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        else:
            return ''
