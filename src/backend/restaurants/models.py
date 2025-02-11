from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    description = models.TextField(verbose_name="Описание")
    cuisine_type = models.CharField(max_length=50, verbose_name="Тип кухни")  # Например, "итальянская", "японская"
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True, verbose_name="Изображение")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0, verbose_name="Рейтинг")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"