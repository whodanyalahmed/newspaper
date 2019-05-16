from django.urls import path,include
from django.contrib import admin
from .views import ( ArticleListView,
                    ArticleDetail,
                    ArticleDelete,
                    ArticleEdit,
                    ArticleCreate)

urlpatterns = [
    path('',ArticleListView.as_view(),name="article_list"),
    path('<int:pk>/edit',ArticleEdit.as_view(),name="article_update"),
    path('<int:pk>/delete',ArticleDelete.as_view(),name="article_delete"),
    path('<int:pk>/',ArticleDetail.as_view(),name="article_detail"),
    path('create',ArticleCreate.as_view(),name="article_create"),
]
