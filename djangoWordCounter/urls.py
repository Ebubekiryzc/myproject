from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='index'),
    path('counter', views.counter, name='counter')
]