from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article
from django.http import Http404, HttpResponseRedirect

 
 
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    template_name = 'about.html'

class NewArticleView(TemplateView):
    template_name = 'AddArticle.html'

def index(request):
    latest_articles_list = Article.objects.order_by('-date_pub')[:5]
    return render(request, 'about.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    return render(request, 'detail.html', { 'article': a} )