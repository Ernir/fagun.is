from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from fagun.models import SidebarEntry, NewsArticle, Recipe, SubPage


class BaseView(View):
    sub_pages = SubPage.objects.filter(visible=True).all()
    params = {
        "sub_pages": sub_pages
    }


class IndexView(BaseView):
    def get(self, request):
        sidebar_entries = SidebarEntry.objects.filter(visible=True).all()
        news_articles = NewsArticle.objects.filter(visible=True).all()[:2]
        recipes = Recipe.objects.filter(visible=True).all()[:2]

        self.params["sidebar_entries"] = sidebar_entries
        self.params["news_articles"] = news_articles
        self.params["recipes"] = recipes

        return render(request, "index.html", self.params)


class ArticleView(BaseView):
    def get(self, request, **kwargs):
        if not "article_slug" in kwargs:
            return self.article_list(request)
        return self.article_detail(request, kwargs["article_slug"])

    def article_list(self, request):
        news_articles = NewsArticle.objects.filter(visible=True).all()
        self.params["article_list"] = news_articles
        return render(request, "news_article_list.html", self.params)

    def article_detail(self, request, slug):
        article = get_object_or_404(NewsArticle, slug=slug)
        self.params["page"] = article

        return render(request, "sub_page.html", self.params)


class RecipeView(BaseView):
    def get(self, request, **kwargs):
        if not "recipe_slug" in kwargs:
            return self.recipe_list(request)
        return self.recipe_detail(request, kwargs["recipe_slug"])

    def recipe_list(self, request):
        recipes = Recipe.objects.filter(visible=True).all()
        self.params["recipe_list"] = recipes
        return render(request, "recipe_list.html", self.params)

    def recipe_detail(self, request, slug):
        article = get_object_or_404(Recipe, slug=slug)
        self.params["page"] = article

        return render(request, "sub_page.html", self.params)


class SubPageView(BaseView):
    def get(self, request, **kwargs):
        page = get_object_or_404(SubPage, slug=self.kwargs["page_slug"])
        self.params["page"] = page

        return render(request, "sub_page.html", self.params)