from django.db import models


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


class NewsArticle(PublishableEntity):
    published_at = models.DateField()
    slug = models.SlugField()

    class Meta:
        ordering = ("published_at", )