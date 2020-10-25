from django.conf.urls import url
from django.urls import path

from .views import index, news_item_detail, news_date

urlpatterns = [
    url(r'^$', index, name='index'),
    path('<int:pk>/', news_item_detail, name='news_item'),
    path('date/', news_date, name='news_date'),
]
