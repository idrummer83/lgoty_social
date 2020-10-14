from django.core.paginator import Paginator
from django.shortcuts import render

from .models import News

# Create your views here.


def index(request):
    news_list = News.objects.all().order_by('id')
    last_news = News.objects.all().reverse()[:6]
    one_news = News.objects.all().reverse()[:1]

    paginator = Paginator(news_list, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        news = paginator.page(page)
    except:
        news = paginator.page(paginator.num_pages)

    context = {
        'news': news,
        'last_news': last_news,
        'one_news': one_news[0]
    }
    return render(request, 'news/news_list.html', context)


def news_item_detail(request, pk):
    news_item = News.objects.filter(pk=pk).first()
    last_news = News.objects.all().reverse()[:5]
    other_news = News.objects.all().reverse()[:3]
    context = {
        'news_item': news_item,
        'last_news': last_news,
        'other_news': other_news
    }
    return render(request, 'news/news_item.html', context)
