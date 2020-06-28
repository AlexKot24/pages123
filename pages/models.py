from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    date_pub = models.DateTimeField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

