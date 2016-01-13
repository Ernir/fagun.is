from django.db import models


class SidebarEntry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(blank=True)
    priority = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name_plural = "sidebar entries"
        ordering = ("priority", )


class Article(models.Model):
    title = models.CharField(max_length=200)
    published_at = models.DateField()
    slug = models.SlugField()
    main_text = models.TextField()

    def __str__(self):
        return self.title