from django.shortcuts import render, get_object_or_404
from django.utils.html import strip_tags
from fagun.models import SidebarEntry, NewsArticle, Recipe, SubPage


def index(request):
    sidebar_entries = SidebarEntry.objects.filter(visible=True).all()

    news_articles = NewsArticle.objects.filter(visible=True).all()[:2]
    recipes = Recipe.objects.filter(visible=True).all()[:2]

    sub_pages = SubPage.objects.filter(visible=True).all()

    return render(request, "index.html", {
        "sidebar_entries": sidebar_entries,
        "news_articles": news_articles,
        "recipes": recipes,
        "sub_pages": sub_pages,
    })


def sub_page(request, page_slug):
    page = get_object_or_404(SubPage, slug=page_slug)
    sub_pages = SubPage.objects.filter(visible=True).all()

    return render(request, "sub_page.html", {
        "page": page,
        "sub_pages": sub_pages,
    })