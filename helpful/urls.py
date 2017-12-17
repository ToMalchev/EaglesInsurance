from django.conf.urls import url, include
from  django.views.generic import ListView, DeleteView
from . import views
from insurance.models import *

urlpatterns = [
    url(r'^$', views.helpful_1, name='helpful'),
]
