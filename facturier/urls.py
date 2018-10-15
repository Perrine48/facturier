"""facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from gestionnaire.views import IndexView, ClientDetailView, ClientUpdateView, ClientCreateView, ClientDeleteView, ProductListView, ProductDetailView, ProductDeleteView, ProductUpdateView, ProductCreateView, QuotationCreateView, QuotationListView, QuotationDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view()),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='/')),

    url(r'^$', IndexView.as_view(), name='dashboard'),

    url(r'^client/(?P<slug>[-\w]+)/$', ClientDetailView.as_view(),
    name='client-detail'),
    url(r'^client/(?P<slug>[-\w]+)/update/$', ClientUpdateView.as_view(), name='client-update'),
    url(r'^client/create', ClientCreateView.as_view(), name='create-client'),
    url(r'^client/(?P<slug>[-\w]+)/delete/$', ClientDeleteView.as_view(), name='client-delete'),

    url(r'^product/$', ProductListView.as_view(), name='product-list'),
    url(r'^product/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(),
    name='product-detail'),
    url(r'^product/create', ProductCreateView.as_view(), name='create-product'),
    url(r'^product/(?P<slug>[-\w]+)/update/$', ProductUpdateView.as_view(), name='product-update'),
    url(r'^product/(?P<slug>[-\w]+)/delete/$', ProductDeleteView.as_view(), name='product-delete'),

    url(r'^quotation/create', QuotationCreateView.as_view(), name='create-quotation'),
    url(r'^quotation/$', QuotationListView.as_view(), name='quotation-list'),
    url(r'^quotation/(?P<ref>[-\w]+)/$', QuotationDetailView.as_view(),
    name='quotation-detail'),
]
