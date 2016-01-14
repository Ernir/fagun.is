__author__ = 'ernir'

from django.conf.urls import url
from fagun import views

urlpatterns = [
    url(r"^$", views.index, name="index"),
    url(r"^undirsida/(?P<page_slug>.+)$", views.sub_page, name="sub_page")
]