from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('page/',views.index,name="page"),
]
