from django.urls import path
from . import views

urlpatterns = [
    # root url, çalıştırıldığında hangi fonksiyonun çalışacağı, şimdilik boş veriyoruz ama bu view' ın adı imiş
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('counter', views.counter, name='counter'),
    # post urline string bir pk isimli parametre vermek:
    path('post/<str:pk>', views.post, name='post')
    # root url + /download:
    #path('/download', views.index, name="index"),
]
