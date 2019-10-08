from django.views.generic import ListView, DetailView

# Create your views here.

from .models import Article

class ArticleList(ListView):
	model = Article
	template_name = 'index.html'

class ArticleView(DetailView):
	template_name = 'detail.html'
	model = Article
	context_object_name = 'article'