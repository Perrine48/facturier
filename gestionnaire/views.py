# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet
from .models import Product, Client, Line, Quotation


# ===================CLIENTS VIEWS===================#
class IndexView(ListView):
    model = Client
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Client.objects.filter(last_name=query)
        else:
            return Client.objects.all()

class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'address', 'zipcode', 'city')
    template_name = 'gestionnaire/client_update_form.html'
    success_url="/"


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    success_url="/"


class ClientDeleteView(DeleteView):
    model = Client
    success_url = "/"


# ===================PRODUCTS VIEWS===================#

class ProductListView(ListView):
    model = Product
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query != None:
            return Product.objects.filter(name=query)
        else:
            return Product.objects.all()

class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    template_name = 'gestionnaire/product_update_form.html'
    success_url="/"


class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url="/"



class ProductDeleteView(DeleteView):
    model = Product
    success_url = "/"


    # ===================QUOTATION VIEWS===================#

class LineInline(InlineFormSet):
    model = Line
    fields = '__all__'

class QuotationCreateView(CreateWithInlinesView):
    template_name = 'gestionnaire/quotation_form.html'
    fields  = '__all__'
    model = Quotation
    inlines = [LineInline, ]
    success_url = "/"


class QuotationListView(ListView):
    model = Quotation
    def get_queryset(self):
        query = self.request.GET.get('q', None)
        statut = self.request.GET.get('p', None)
        if query != None:
            if statut is not None:
                return Quotation.objects.filter(statut__icontains=statut, client__first_name__icontains=query)
            else:
                return Quotation.objects.filter(client__first_name__icontains=query)
        else:
            return Quotation.objects.all()


class QuotationDetailView(DetailView):
    model = Quotation
    slug_field = "ref"
    slug_url_kwarg = "ref"

    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        context['lineDetail'] = Line.objects.all().filter(quotation = self.object)
        return context


class QuotationUpdateView(UpdateView):
    model = Quotation
