from django.urls import path, include
from django.contrib import admin
from .import views


urlpatterns = [
    path('', views.index, name='home'),
    path('today-rota', views.today_rota, name='today-rota'),
    path('announcements', views.annoucements, name='announcements'),
]
