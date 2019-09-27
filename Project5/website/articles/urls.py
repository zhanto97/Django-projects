from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleList.as_view(), name = 'index'),
    path('article/<int:pk>', views.ArticleView.as_view(), name = 'article_page'),
    path('article/new/', views.ArticleCreateView.as_view(), name = 'new_article'),
    path('article/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name = 'article_edit'),
    path('article/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name = 'article_delete'),
]
