from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    restaurant = models.ForeignKey('restaurants.Restaurant', on_delete=models.CASCADE, verbose_name="Ресторан")
    booking_date = models.DateTimeField(verbose_name="Дата бронирования")
    guest_count = models.PositiveIntegerField(default=1, verbose_name="Количество гостей")
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Ожидает подтверждения'), ('confirmed', 'Подтверждено'), ('rejected', 'Отклонено')],
        default='pending',
        verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Бронь {self.user.username} в {self.restaurant.name}"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
