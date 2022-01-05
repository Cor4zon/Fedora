from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        # Определили модель для сериализации
        model = Person
        # Оперделили список полей для сериализации
        fields = ["id", "first", "last", "title"]