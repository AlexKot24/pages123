# pages/urls.py
from django.urls import path
 
from .views import HomePageView, AboutPageView, index, detail

urlpatterns = [
    path('about/', index, name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('about/<int:article_id>/', detail, name='detail'),
]