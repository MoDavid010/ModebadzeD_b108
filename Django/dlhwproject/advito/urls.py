from django.urls import path
from .views import index

urlpatterns = [

    path('1/', index, name='index'),
    path('2/', index, name='index2'),


]
