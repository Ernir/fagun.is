from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from fagun.models import SidebarEntry, NewsStory, EducationalArticle, SubPage, Tag


class BaseView(View):
    sub_pages = SubPage.objects.filter(visible=True).all()
    params = {
        "sub_pages": sub_pages
    }


class IndexView(BaseView):
    def get(self, request):
        sidebar_entries = SidebarEntry.objects.filter(visible=True).all()
        news_stories = NewsStory.objects.filter(visible=True).all()[:2]
        articles = EducationalArticle.objects.filter(visible=True).all()[:2]

        self.params["sidebar_entries"] = sidebar_entries
        self.params["news_stories"] = news_stories
        self.params["edu_articles"] = articles

        return render(request, "index.html", self.params)


class NewsStoryView(BaseView):
    def get(self, request, **kwargs):
        if not "news_slug" in kwargs:
            return self.news_list(request)
        return self.news_detail(request, kwargs["news_slug"])

    def news_list(self, request):
        news_stories = NewsStory.objects.filter(visible=True).all()
        self.params["news_stories"] = news_stories
        return render(request, "news_story_list.html", self.params)

    def news_detail(self, request, slug):
        article = get_object_or_404(NewsStory, slug=slug)
        self.params["page"] = article

        return render(request, "sub_page.html", self.params)


class EducationalArticleView(BaseView):
    def get(self, request, **kwargs):
        if not "article_slug" in kwargs:
            return self.educational_article_list(request)
        return self.educational_article_detail(request, kwargs["article_slug"])

    def educational_article_list(self, request):
        articles = EducationalArticle.objects.filter(visible=True).all()
        self.params["edu_articles"] = articles
        return render(request, "edu_article_list.html", self.params)

    def educational_article_detail(self, request, slug):
        article = get_object_or_404(EducationalArticle, slug=slug)
        self.params["page"] = article

        return render(request, "sub_page.html", self.params)


class SubPageView(BaseView):
    def get(self, request, **kwargs):
        page = get_object_or_404(SubPage, slug=self.kwargs["page_slug"])
        self.params["page"] = page
        self.params["show_tags"] = False

        return render(request, "sub_page.html", self.params)


class TagView(BaseView):
    def get(self, request, **kwargs):
        tag = get_object_or_404(Tag, slug=self.kwargs["tag_slug"])

        stories = NewsStory.objects.filter(tags__slug=tag.slug).all()
        articles = EducationalArticle.objects.filter(tags__slug=tag.slug).all()

        self.params["tag"] = tag
        self.params["news_stories"] = stories
        self.params["edu_articles"] = articles

        return render(request, "tag_list.html", self.params)