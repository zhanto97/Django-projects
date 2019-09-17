from django.views.generic import ListView

from .models import Cmdr

class HomePage(ListView):
	model = Cmdr
	template_name = 'index.html'