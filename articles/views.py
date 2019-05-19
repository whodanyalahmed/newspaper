from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.http import HttpResponse,request
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "article.html"
    model = Article
    login_url= 'login'


class ArticleEdit(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title','body',)
    template_name = "article_edit.html"
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ArticleDetail(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_detail.html"
    login_url = 'login'

class ArticleDelete(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreate(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ('title','body')
    login_url = 'login'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
