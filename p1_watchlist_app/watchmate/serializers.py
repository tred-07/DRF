from rest_framework import serializers
from .models import Movie
class MovieSerializer(serializers.Serializer): # General Serializer
    id=serializers.IntegerField(read_only=True)
    name=serializers.CharField()
    description=serializers.CharField()
    active=serializers.BooleanField(read_only=True)
    

    def create(self,validated_data):  # create method
        movie = Movie.objects.create(**validated_data)
        return movie   

    def update(self, instance, validated_data): # update method
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance 


class MovieModelSerializer(serializers.ModelSerializer): # Model serializer . Don not need crud method. This is the benefit of model serializers.
    class Meta:
        model=Movie # select Model
        # fields=['name','description'] # select fields
        exclude=['name','description']
