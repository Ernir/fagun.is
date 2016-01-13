from django.shortcuts import render
from fagun.models import SidebarEntry, NewsArticle


def index(request):

    sidebar_entries = SidebarEntry.objects.all()
    news_articles = NewsArticle.objects.all()

    return render(request,"index.html", {
        "sidebar_entries": sidebar_entries,
        "news_articles": news_articles
    })