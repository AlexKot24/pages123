# pages/urls.py
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
 
from .views import HomePageView, index, detail, home

urlpatterns = [
    path('about/', index, name='about'),
    path('', home, name='home'),
    path('about/<int:article_id>/', detail, name='detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)