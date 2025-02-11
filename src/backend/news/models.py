from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    short_description = models.CharField(max_length=255, verbose_name="Краткое описание")
    content = models.TextField(verbose_name="Содержание")
    image = models.ImageField(upload_to='news/', null=True, blank=True, verbose_name="Изображение")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
