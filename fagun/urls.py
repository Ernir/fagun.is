__author__ = 'ernir'

from django.conf.urls import url
from fagun import views

urlpatterns = [
    url(r"^$", views.IndexView.as_view(), name="index"),
    url(r"^frettir/$", views.ArticleView.as_view(), name="news_list"),
    url(r"^frettir/(?P<article_slug>.+)/$", views.ArticleView.as_view(), name="news_article"),
    url(r"^uppskriftir/$", views.RecipeView.as_view(), name="recipe_list"),
    url(r"^uppskriftir/(?P<recipe_slug>.+)/$", views.RecipeView.as_view(), name="recipe"),
    url(r"^(?P<page_slug>.+)/$", views.SubPageView.as_view(), name="sub_page")
]