from django.db import models
from django.db.models import Prefetch


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Article(models.Model):
    date = models.DateField()


class ArticleTranslate(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.language.name + ' - article: ' + self.article.pk



