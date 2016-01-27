from django.db import models
from django.utils.text import slugify


class PublishableEntity(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class SidebarEntry(PublishableEntity):
    priority = models.PositiveIntegerField(default=0)

    class Meta(object):
        verbose_name_plural = "sidebar entries"
        ordering = ("priority", )


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    class Meta:
        ordering = ("name", )


class NewsStory(PublishableEntity):
    published_at = models.DateField()
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(NewsStory, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-published_at", )


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EducationalArticle(PublishableEntity):
    published_at = models.DateField()
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(EducationalArticle, self).save(*args, **kwargs)

    class Meta:
        ordering = ("-published_at", )


class SubPage(PublishableEntity):
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubPage, self).save(*args, **kwargs)