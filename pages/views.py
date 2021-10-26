# from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutMeView(TemplateView):
    template_name = "about.html"    