"""pilga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static

from pilga_project.views import index, search_page, search_request, privilege_item, institutions,\
    institution_item, about, feedback, subscribe, download_csv


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    url(r'^$', index, name='index'),
    path('search', search_page, name='search'),
    path('subscribe', subscribe, name='subscribe'),
    path('download_csv', download_csv, name='download_csv'),
    path('about', about, name='about'),
    path('feedback', feedback, name='feedback'),
    # path('send_feedback', send_feedback, name='send_feedback'),
    path('search_request', search_request, name='search_request'),
    path('institutions', institutions, name='institutions'),
    path('institution/<str:slug>/', institution_item, name='institution_item'),

    path('privilege/<str:slug>', privilege_item, name='privilege_item'),
    url(r'^news/', include(('news.urls', 'news'), namespace='news')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

