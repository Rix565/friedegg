from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:postid>/', views.post_view, name='posts'),
]