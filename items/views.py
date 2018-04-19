# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from models import Item, Photo
from gallery.settings import ROOT_URL


# Create your views here.
class ItemIndexView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'item_list'


class ItemListView(ListView):
    model = Item
    template_name = 'items_list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items_detail.html'


class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photos_detail.html'
    context_object_name = 'object'


# for templates, to get static file path
def root_url_processor(request):
    return {'ROOT_URL': ROOT_URL}
