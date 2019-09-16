from django.views.generic import TemplateView

class HomePage(TemplateView):
	template_name = 'index.html'

class AboutUsPage(TemplateView):
	template_name = 'about.html'

class ContactUsPage(TemplateView):
	template_name = 'contact.html'

