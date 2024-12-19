from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets
from .serializers import MovieModelSerializer,MovieSerializer
from rest_framework import decorators,response
# Create your views here.


# def movie_list(request):
#     movies = Movie.objects.all() # it creates all objects from model
#     print (movies.values()) # prints all objects
#     data={'movies':list(movies.values())} # converts all objects to json
#     return JsonResponse(data) # returns json response

def movie_detail(request, pk):
    try:
        movies = Movie.objects.get(pk=pk) # it fetches a single object by id
        data = {
            'name':movies.name,
            'description':movies.description,
            'active':movies.active, 
        } # converts object to json
    except Movie.DoesNotExist:
        return HttpResponse(status=404) # returns 404 if movie not found
    return JsonResponse(data) # returns json response

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer # using serializer from serializers.py

@decorators.api_view(['GET']) # from rest_framework import decorators
def movie_list(request):
    movie=Movie.objects.all()
    serializer=MovieSerializer(movie,many=True) # many=true means it check all object of serializer individually.
    return response.Response(serializer.data)