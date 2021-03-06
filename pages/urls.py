# pages/urls.py
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from .views import HomePageView, index, detail, home, createarticle

urlpatterns = [
    path('about/', index, name='about'),
    path('', home, name='home'),
    path('about/<int:article_id>/', detail, name='detail'),
    path('create_article/', createarticle, name='createarticle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()