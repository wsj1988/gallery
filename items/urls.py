# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from views import ItemIndexView, ItemListView, ItemDetailView, PhotoDetailView

urlpatterns = [
    url(r'^$', ItemIndexView.as_view(), name='index'),
    url(r'^items/$', ItemListView.as_view(), name='item_list'),
    url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),
    url(r'^photos/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo_detail'),
]
