from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'

    def validate_title(self,data):
        if data=="abc":
            raise serializers.ValidationError("No abc please")
        return data

    def validate(self,data):
        if data['no_of_pages']>200 and data['quantity']>200:

            raise serializers.ValidationError("Too much for the store")
        return data