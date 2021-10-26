from django.urls import path

from pages.views import AboutMeView
from .views import HomePageView, AboutMeView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutMeView.as_view(),name='about'), 
]
