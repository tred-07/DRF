from django.shortcuts import render,redirect
from .models import Movie
from django.http import HttpResponse,JsonResponse
from rest_framework import viewsets,views
from .serializers import MovieModelSerializer,MovieSerializer
from rest_framework import decorators,response,status

# Create your views here.

class movie_list(views.APIView):

    def get(self,request): # instead of get condition and can not use if serializer.is_valid() in get method
        movies=Movie.objects.all()
        serializer=MovieModelSerializer(movies,many=True)
        return response.Response(serializer.data)
        
    def post(self,request): 
        serializer=MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)


class movie_detail(views.APIView):
    def get(self,request,pk): # r = read operation
        movie=Movie.objects.get(pk=pk)
        serializer=MovieModelSerializer(movie)
        return response.Response(serializer.data)
    
    def post(self,request): # c = create operation
        serializer=MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)
        
    def put(self,request,pk): # u = update operation
        movie=Movie.objects.get(pk=pk)
        serializer=MovieModelSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
            # return redirect('movie_list')
        else:
            return response.Response(serializer.errors)
            # return redirect('movie_detail')    
        
    def delete(self,request,pk): # d = delete operation
            movie=Movie.objects.get(pk=pk)
            movie.delete()
            return redirect('movie_list')





# def movie_list(request):
#     movies = Movie.objects.all() # it creates all objects from model
#     print (movies.values()) # prints all objects
#     data={'movies':list(movies.values())} # converts all objects to json
#     return JsonResponse(data) # returns json response


# @decorators.api_view(['GET','POST','DELETE','PUT'])
# def movie_detail(request, pk):
#     if request.method=='GET':
#         try:
#             movies = Movie.objects.get(pk=pk) # it fetches a single object by id
#             serializer=MovieSerializer(movies)
#         except Movie.DoesNotExist:
#             return HttpResponse(status=404) # returns 404 if movie not found
#         return response.Response(serializer.data) # returns json response
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('movie_list')
#         return HttpResponse('Something went wrong')
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data)
#         else:
#             return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return response.Response(status=status.HTTP_204_NO_CONTENT)


# @decorators.api_view(['GET','POST']) # from rest_framework import decorators
# def movie_list(request):
#     if request.method=='GET':
#         movie=Movie.objects.all()
#         serializer=MovieSerializer(movie,many=True) # many=true means it check all object of serializer individually.
#         return response.Response(serializer.data)
#     if request.method=='POST':
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return redirect('movie_list')
#         return HttpResponse('Something went wrong')