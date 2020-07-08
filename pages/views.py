from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, ImageGallery
from django.http import Http404, HttpResponseRedirect

 
 
class HomePageView(TemplateView):
    template_name = 'home.html'

# class AboutPageView(TemplateView):
#     latest_articles_list = Article.objects.order_by('-pub_date')[:5]
#     template_name = 'about.html'

class NewArticleView(TemplateView):
    template_name = 'AddArticle.html'

def home(request):
    latest_articles_list = Article.objects.order_by('-date_pub')[0:3]
    #   article_photo = latest_articles_list.imagegallery_set.all()[:1];
    return render(request, 'home.html', {'latest_articles_list': latest_articles_list }) # 'article_photo': article_photo

def index(request):
    latest_articles_list = Article.objects.order_by('-date_pub')
    return render(request, 'about.html', {'latest_articles_list': latest_articles_list})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    return render(request, 'detail.html', { 'article': a} )

def createarticle (request):
    return render(request, 'createarticle.html')