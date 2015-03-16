from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    published_at = models.DateField()
    slug = models.SlugField()
    main_text = models.TextField()

    def __str__(self):
        return self.title