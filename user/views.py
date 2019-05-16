from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CustomUserChangeForm
from django.views.generic import CreateView 

class SignUpView(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    template_name = "signup.html"



# Create your views here.
