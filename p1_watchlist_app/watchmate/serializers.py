from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.Serializer): # General Serializer
    class Meta:
        model=Movie # Select Model
        fields='__all__' # List of fields


class MovieModelSerializer(serializers.ModelSerializer): # Model serializer
    class Meta:
        model=Movie # select Model
        fields='__all__' # select fields
