from django.urls import path, include

from . import views

urlpatterns = [
    path('greet', views.hello_world_view, name='greet'),
    path('person', views.hello_Joseph_view, name='person'),
    path('index', views.html_view, name='index'),
]
