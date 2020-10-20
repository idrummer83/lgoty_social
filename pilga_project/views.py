from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Prefetch
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator

import csv

from .models import Slider, Privilege, PrivilegeType, Group, SubGroup, Region, DocumentType, IssuedBy, Agency,\
    About, Subscribe
from .forms import SubscribeForm, FeedBackForm
from news.models import News

from .filters import PilgaFilter

# Create your views here.


def index(request):
    slider = Slider.objects.all()
    news = News.objects.filter(main_page=True)
    last_news = News.objects.all().reverse()[:6]
    privilege_type = PrivilegeType.objects.all()
    group = Group.objects.all()
    subgroup = SubGroup.objects.all()

    context = {
        'main_slider': slider,
        'news': news,
        'last_news': last_news,
        'privilege_type': privilege_type,
        'group': group,
        'subgroup': subgroup,
    }
    return render(request, 'pilga_project/index.html', context)


def about(request):
    about = About.objects.all().first()
    context = {
        'about': about,
    }
    return render(request, 'pilga_project/about.html', context)


def feedback(request):
    privilege_type = PrivilegeType.objects.all()
    if request.method == 'POST':
        form = FeedBackForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение успешно отправлено администрации сайта и будет рассмотрено в ближайшrее время.')
        else:
            email = [i for i in form.errors['email'].as_data()]
            messages.error(request, email, fail_silently=True)

    context = {
        'privilege_type': privilege_type,
    }
    return render(request, 'pilga_project/feedback_form.html', context)


def search_page(request):
    privilege = Privilege.objects.all()
    privilege_type = PrivilegeType.objects.all()
    group = Group.objects.all()
    subgroup = SubGroup.objects.all()
    region = Region.objects.all()
    document_type = DocumentType.objects.all()

    context = {
        'privilege': privilege,
        'privilege_type': privilege_type,
        'group': group,
        'subgroup': subgroup,
        'region': region,
        'document_type': document_type,
    }
    return render(request, 'pilga_project/pilga_search_form.html', context)


def search_request(request):
    # if request.POST:
    #     print('req', request.POST)
    #
    #     obj = request.POST.copy()
    #     obj.pop('csrfmiddlewaretoken')
    #
    #     search = Q()
    #     for key, value in obj.items():
    #         search.add(Q("{}={}".format(key, value)))
    #         # search.add(Q(**{key: value}), Q.OR)
    #     print('sss', search)
    #     p = Privilege.objects.filter(search)

    p_filter = PilgaFilter(request.GET, queryset=Privilege.objects.all())

    paginator = Paginator(p_filter.qs.order_by('id'), 2)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        result = paginator.page(page)
    except:
        result = paginator.page(paginator.num_pages)

    privilege = Privilege.objects.all()
    privilege_type = PrivilegeType.objects.all()
    group = Group.objects.all()
    subgroup = SubGroup.objects.all()
    region = Region.objects.all()
    document_type = DocumentType.objects.all()

    context = {
        'privilege': privilege,
        'privilege_type': privilege_type,
        'group': group,
        'subgroup': subgroup,
        'region': region,
        'document_type': document_type,

        'result': result,
        'count': len(p_filter.qs),
    }
    return render(request, 'pilga_project/pilga_search_result.html', context)


def privilege_item(request, slug):
    item = Privilege.objects.filter(title=slug).prefetch_related(Prefetch('agency')).first()
    context = {
        'privilege': item,
    }
    return render(request, 'pilga_project/privilege_item.html', context)


def institutions(request):
    agencies = Agency.objects.all()
    context = {
        'agencies': agencies
    }
    return render(request, 'pilga_project/agencies_list.html', context)


def institution_item(request, slug):
    agency = Agency.objects.filter(agency=slug).first()
    context = {
        'agency': agency
    }
    return render(request, 'pilga_project/agency_item.html', context)


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.errors:
            messages.error(request, 'jhgfjhgfjhgf', extra_tags='form')
            return HttpResponseRedirect('/')
        if form.is_valid():
            form.save()
            messages.success(request, 'Your subscribe saved successfully!')
            return redirect('/')


def download_csv(request):
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=subscribe_list.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Phone', 'Email'])
    for item in Subscribe.objects.all():
        writer.writerow([item.name, item.phone, item.email])
    return response
