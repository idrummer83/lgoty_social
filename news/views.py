from django.shortcuts import render
from django.db.models import Prefetch, Q
from django.http import Http404, HttpResponsePermanentRedirect
from django.core.paginator import Paginator

from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView

from .models import News, NewsImage

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


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    paginate_by = 6
    context_object_name = 'news'
    queryset = News.objects.prefetch_related(
        Prefetch(
            'news_images',
            NewsImage.objects.all()
        )
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_object = News.objects.filter(slug='news').first()
        # context.update(
        #     seo_dict_generate(page_object, self.request, page_object, pagination=context['page_obj'].number)
        # )
        context['last_news'] = self.queryset[:3]
        return context


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



# @require_http_methods(['GET'])
def n111111111111ews_item_detail(request, slug):
    news_item = get_object_or_404(
        News.objects.prefetch_related(
            Prefetch(
                'news_images',
                NewsImage.objects.all()
            )
        ),
        slug=slug
    )

    if news_item.outer_url:
        return HttpResponsePermanentRedirect(news_item.outer_url)

    news = News.objects.published()[:6]
    ctx = {
        'news_item': news_item,
        'last_news': news
    }
    page_object = News.objects.filter(slug='news').first()
    # ctx.update(seo_dict_generate(news_item, request, page_object))

    return render(request, 'news/news_item.html', ctx)
