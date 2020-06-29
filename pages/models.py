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

# from pages.models import ImageGallery

class ImageGallery(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images/')
    gallery = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'