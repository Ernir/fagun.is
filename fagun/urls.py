__author__ = 'ernir'

from django.conf.urls import url
from fagun import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^frettir/$", views.NewsStoryView.as_view(), name="news_list"),
    url(r"^frettir/(?P<news_slug>.+)/$", views.NewsStoryView.as_view(), name="news_story"),
    url(r"^greinar/$", views.EducationalArticleView.as_view(), name="edu_article_list"),
    url(r"^greinar/(?P<article_slug>.+)/$", views.EducationalArticleView.as_view(), name="article"),
    url(r"^flokkar/(?P<tag_slug>.+)/$", views.TagView.as_view(), name="tag"),
    url(r"^internals/mail-register/$", views.MailView.as_view(), name="mail"),
    url(r"^(?P<page_slug>.+)/$", views.SubPageView.as_view(), name="sub_page"),
]