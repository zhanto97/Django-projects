from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name = 'index'),
    path('article/<int:pk>', views.ArticleView.as_view(), name = 'article_page'),
]
