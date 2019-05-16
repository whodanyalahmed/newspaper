from django.shortcuts import render
from django.http import request,HttpResponse

# Create your views here.

def index(request):
    render("base.html")