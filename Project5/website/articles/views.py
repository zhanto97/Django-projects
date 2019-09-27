from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

from .models import Article

class ArticleList(ListView):
	model = Article
	template_name = 'index.html'

class ArticleView(DetailView):
	template_name = 'detail.html'
	model = Article
	context_object_name = 'article'

class ArticleCreateView(CreateView):
	model = Article
	template_name = 'article_new.html'
	fields = '__all__'

class ArticleUpdateView(UpdateView):
	model = Article
	template_name = 'article_edit.html'
	fields = ['title', 'text']

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = 'article_delete.html'
	context_object_name = 'article'
	success_url = reverse_lazy('index')