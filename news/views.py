from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render
from django.template.loader import render_to_string

import json

from .models import News
from .forms import NewsForm

# Create your views here.


def index(request):
    last_news = News.objects.all().reverse()[:6]
    one_news = News.objects.all().reverse()[:1]

    if request.method == 'GET':
        form = NewsForm(request.GET or None)
        if form.is_valid():
            search_title = request.GET.get('title', None)
            news_list = News.objects.filter(title__icontains=search_title)
            context = {
                'news': news_list,
                'last_news': last_news,
                'one_news': one_news[0]
            }
            return render(request, 'news/news_page.html', context)

    news_list = News.objects.all().order_by('id')
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
    return render(request, 'news/news_page.html', context)


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


def news_date(request):
    if request.method == 'POST':
        news_list = News.objects.filter(
            Q(created_at__day=request.POST['news_date'][:2]), Q(created_at__month=request.POST['news_date'][3:5])
        )
        rendered = render_to_string('news/news_list.html', {'news': news_list})
        result = JsonResponse(rendered, safe=False)
        mimetype = 'application/json'
        return HttpResponse(result, mimetype)
