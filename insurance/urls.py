from django.conf.urls import url, include
from  django.views.generic import ListView, DeleteView
from . import views
from insurance.models import *

urlpatterns = [
    url(r'^$', views.insurance, name="insurance"),
    url(r'^(?P<pk_ins>[-\d]+)/$', views.insurance1, name="insurance1"),
    url(r'^[0-9]/(?P<type_insurance>[-\w]+)/', views.insurance_type, name="insurance_t"),
]