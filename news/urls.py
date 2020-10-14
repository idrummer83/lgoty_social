from django.conf.urls import url
from django.urls import path

from .views import index, news_item_detail

urlpatterns = [
    url(r'^$', index, name='index'),
    path('<int:pk>/', news_item_detail, name='news_item'),
]
