from rest_framework import serializers
from .models import WatchList,StreamPlatform

class WatchListSerializer(serializers.ModelSerializer): # Model serializer . Don not need crud method. This is the benefit of model serializers.
    class Meta:
        model=WatchList # select Model
        fields='__all__'


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    watchlist=WatchListSerializer(many=True,read_only=True)
    class Meta:
        model=StreamPlatform
        fields='__all__'