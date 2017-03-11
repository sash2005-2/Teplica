from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.index, name='index_tpl'),
    url(r'^delivery/', views.delivery, name='delivery_tpl'),
    url(r'^pay/', views.pay, name='pay_tpl'),
    url(r'^contact/', views.contact, name='contact_tpl'),
]
