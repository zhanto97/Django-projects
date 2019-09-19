from django.views.generic import ListView

# Create your views here.

from .models import Article

class ArticleList(ListView):
	model = Article
	template_name = 'index.html'