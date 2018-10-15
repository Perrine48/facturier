# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Client, Product, Line, Quotation


class ProductAdmin(admin.ModelAdmin):
   list_display = ('id', 'name', 'description', 'price', 'cover', 'stock', 'slug')
   search_fields = ('name', 'price', 'stock')


class ClientAdmin(admin.ModelAdmin):
   list_display = ('id', 'first_name', 'last_name', 'address', 'zipcode', 'city', 'email')


class LineInline(admin.TabularInline):
    model = Line


class QuotationAdmin(admin.ModelAdmin):
   inlines = [LineInline, ]
   list_display = ('id', 'ref', 'client', 'create_date', 'statut')




admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Quotation, QuotationAdmin)
