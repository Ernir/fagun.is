__author__ = 'ernir'

from django.conf.urls import patterns, url
from fagun import views

urlpatterns = patterns('',
                       url(r"^$", views.index, name="index")
)