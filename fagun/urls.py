__author__ = 'ernir'

from django.conf.urls import url
from fagun import views

urlpatterns = [
    url(r"^$", views.index, name="index")
]