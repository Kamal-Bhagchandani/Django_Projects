from django.contrib import admin
from django.urls import include, path
from . import views
urlpatterns = [
    path('createPost/', views.createPost, name='createPost'),
    path('uploadPost/', views.uploadPost, name='uploadPost'),
    path('viewPost/', views.viewPost, name='viewPost'),
    path('deletePost/<id>',views.deletePost,name='deletePost'),
]
