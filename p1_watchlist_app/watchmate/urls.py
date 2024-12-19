from django.shortcuts import render
from django.urls import URLPattern,include,path
from .views import movie_list,movie_detail
urlpatterns=[
    path('list/',movie_list,name='movie_list'),
    path('list/<int:pk>',movie_detail),  # it searches for specific id
]