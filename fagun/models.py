from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class PublishableEntity(models.Model):
    """
    An abstract class encapsulating behaviour common among sub-pages,
    articles and news stories.
    """
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField(blank=True)
    visible = models.BooleanField(default=True)
    slug = models.SlugField(max_length=50)

    def make_unique_slug(self):
        # ToDo: guarantee uniqueness among all objects
        return slugify(self.title)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class SidebarEntry(PublishableEntity):
    """
    An entry to be displayed on the front page.
    """
    priority = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = self.make_unique_slug()
        super(SidebarEntry, self).save(*args, **kwargs)

    class Meta(object):
        verbose_name_plural = "sidebar entries"
        ordering = ("priority", )


class Tag(models.Model):
    """
    A "vertical" category for articles and stories, associated with
    each via a N-N relationship.
    """
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("tag", args=[self.slug])

    def make_unique_slug(self):
        max_length_base = 50
        n_similar = Tag.objects.filter(name=self.name).count()
        slug_base = slugify(self.name)
        if n_similar <= 1:
            return slug_base
        else:
            max_length = max_length_base - len(str(n_similar)) - 1
            return slug_base[:max_length] + "-" + str(n_similar)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.make_unique_slug()
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ("name", )


class NewsStory(PublishableEntity):
    """
    One news story/article/blog, intended for one-time publishing
    """
    published_at = models.DateField()
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("news_story", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = self.make_unique_slug()
        super(NewsStory, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "news stories"
        ordering = ("-published_at", )


class Author(models.Model):
    """
    Each article is associated with an author, independent of Django users
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EducationalArticle(PublishableEntity):
    """
    An instructional article, such as a recipe.
    """
    published_at = models.DateField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("article", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = self.make_unique_slug()
        super(EducationalArticle, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-published_at", )


class SubPage(PublishableEntity):
    """
    Sub-pages containing arbitrary admin-defined HTML.
    """

    def get_absolute_url(self):
        return reverse("sub_page", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubPage, self).save(*args, **kwargs)