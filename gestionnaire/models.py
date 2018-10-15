# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from autoslug import AutoSlugField


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='first_name', unique_with=['last_name'])
    address = models.CharField(max_length=120)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=70)
    email = models.EmailField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name


class Product(models.Model):
    name = models.CharField(max_length=80)
    slug = AutoSlugField(populate_from='name')
    description = models.CharField(max_length=200)
    price = models.FloatField()
    cover = models.ImageField(upload_to="articles", blank=True, null=True)
    stock = models.IntegerField()

    def __unicode__(self):
        return self.name


class Quotation(models.Model):
    ref = models.CharField(max_length=80)
    client = models.ForeignKey(Client)
    create_date = models.DateField(auto_now_add=True)
    statut = models.CharField(choices=(
    ('PROGRESS', 'In progress'),
    ('RECALL', 'In recall'),
    ('DONE', 'Done'),
    ), default=None, max_length=20)

class Line(models.Model):
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()
    quotation = models.ForeignKey(Quotation)

    def multiply(self):
        return self.quantity * self.product.price
