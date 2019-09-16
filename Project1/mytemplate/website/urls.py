from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='index'),
    path('about/', views.AboutUsPage.as_view(), name='about'),
    path('contact/', views.ContactUsPage.as_view(), name='contact'),
]
