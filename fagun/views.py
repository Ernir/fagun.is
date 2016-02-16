from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from fagun.forms import MailForm
from fagun.mail_chimp import MailChimp
from fagun.models import SidebarEntry, NewsStory, EducationalArticle, \
    SubPage, Tag


class BaseView(View):
    """
    An "abstract view" to manage the elements all of the site's
    pages have in common
    """

    def __init__(self):
        super().__init__()
        sub_pages = SubPage.objects.filter(visible=True).all()
        self.params = {
            "sub_pages": sub_pages,
            "title": "Fágun",  # Default value
            "sub_title": ""
        }


class IndexView(BaseView):
    """
    A view for the site's index page
    """

    def get(self, request):
        sidebar_entries = SidebarEntry.objects.filter(visible=True).all()
        news_stories = NewsStory.objects.filter(visible=True).all()[:2]
        articles = EducationalArticle.objects.filter(visible=True).all()[
                   :2]
        mail_form = MailForm()

        self.params["sidebar_entries"] = sidebar_entries
        self.params["news_stories"] = news_stories
        self.params["edu_articles"] = articles
        self.params["mail_form"] = mail_form
        self.params["sub_title"] = "Félag áhugafólks um gerjun"

        return render(request, "index.html", self.params)


class NewsStoryView(BaseView):
    """
    Views for news stories, both individual and a list
    """

    def get(self, request, **kwargs):
        if not "news_slug" in kwargs:
            return self.news_list(request)
        return self.news_detail(request, kwargs["news_slug"])

    def news_list(self, request):
        news_stories = NewsStory.objects.filter(visible=True).all()
        self.params["news_stories"] = news_stories
        self.params["title"] = "Fréttir"
        return render(request, "news_story_list.html", self.params)

    def news_detail(self, request, slug):
        article = get_object_or_404(NewsStory, slug=slug)
        self.params["page"] = article
        self.params["title"] = article.title
        self.params["sub_title"] = article.sub_title

        return render(request, "sub_page.html", self.params)


class EducationalArticleView(BaseView):
    """
    Views for articles, both individual and a list
    """

    def get(self, request, **kwargs):
        if not "article_slug" in kwargs:
            return self.educational_article_list(request)
        return self.educational_article_detail(request,
                                               kwargs["article_slug"])

    def educational_article_list(self, request):
        articles = EducationalArticle.objects.filter(visible=True).all()
        self.params["edu_articles"] = articles
        self.params["title"] = "Greinar"
        return render(request, "edu_article_list.html", self.params)

    def educational_article_detail(self, request, slug):
        article = get_object_or_404(EducationalArticle, slug=slug)
        self.params["page"] = article
        self.params["title"] = article.title
        self.params["sub_title"] = article.sub_title

        return render(request, "sub_page.html", self.params)


class SubPageView(BaseView):
    """
    A view defining a sub page containing generic editable HTML content.
    """

    def get(self, request, **kwargs):
        page = get_object_or_404(SubPage, slug=self.kwargs["page_slug"])
        self.params["page"] = page
        self.params["show_tags"] = False
        self.params["title"] = page.title
        self.params["sub_title"] = page.sub_title

        return render(request, "sub_page.html", self.params)


class TagView(BaseView):
    """
    A view to see all news and articles associated with a given tag.
    """

    def get(self, request, **kwargs):
        tag = get_object_or_404(Tag, slug=self.kwargs["tag_slug"])

        stories = NewsStory.objects.filter(tags__slug=tag.slug).all()
        articles = EducationalArticle.objects.filter(
            tags__slug=tag.slug).all()

        self.params["tag"] = tag
        self.params["title"] = tag.name
        self.params["sub_title"] = \
            'Allar fréttir og greinar sem tengjast "{}"'.format(tag.name)
        self.params["news_stories"] = stories
        self.params["edu_articles"] = articles

        return render(request, "tag_list.html", self.params)


class MailView(View):
    """
    A view handling the mailing list registration form on the index page.
    """

    def post(self, request):
        ## ToDo: Actually register that someone
        mail_helper = MailChimp()
        email_address = request.POST["user_email"]

        code = mail_helper.add_member(email_address)
        if code == 200:
            response = "<p>Takk fyrir að skrá þig á póstlista Fágunar!" \
                       "Þú munt fá næsta fréttabréf þegar það kemur út." \
                       "</p>"
        else:
            response = "<p>Villa kom upp við sjálfvirka skráningu. " \
                       "Vinsamlegast reyndu aftur síðar eða hafðu " \
                       "samband við fagun@fagun.is til að biðja um " \
                       "handvirka skráningu.</p>"

        return JsonResponse({"response": response})
