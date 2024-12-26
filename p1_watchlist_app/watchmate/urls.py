# from django.shortcuts import render
# from django.urls import URLPattern,include,path
# from .views import movie_list,movie_detail,StreamListAV,StreamDetailAV
# urlpatterns=[
#     path('watchlist/',movie_list.as_view(),name='movie_list'),
#     path('watchlist/<int:pk>',movie_detail.as_view(),name='movie_detail'),  # it searches for specific id
#     path('streamlist/',StreamListAV.as_view(),name='stream_list'),
#     path('streamlist/<int:pk>',StreamDetailAV.as_view(),name='stream_detail')
# ]