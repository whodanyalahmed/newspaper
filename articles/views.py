from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from django.views.generic.edit import UpdateView,DeleteView
from django.http import HttpResponse,request
from django.urls import reverse_lazy
from .models import Article
# Create your views here.

class ArticleListView(ListView):
    template_name = "article.html"
    model = Article

class ArticleEdit(UpdateView):
    model = Article
    fields = ('title','body',)
    template_name = "article_edit.html"


class ArticleDetail(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleDelete(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')

class ArticleCreate(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ('title','body','author')
