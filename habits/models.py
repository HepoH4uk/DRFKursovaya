from django.db import models

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="habits"
    )
    place = models.CharField(
        max_length=100,
        help_text="Укажите место, в котором необходимо выполнять привычку"
    )
    time = models.TimeField(
        help_text="Укажите время, когда необходимо выполнять привычку"
    )
    action = models.CharField(
        max_length=100,
        help_text="Укажите действие, которое представляет собой привычка"
    )
    is_pleasant = models.BooleanField(
        default=False,
        help_text="Привычка, которую можно привязать к выполнению полезной привычки."
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={"is_pleasant": True},
        help_text="Привычка, которая связана с другой полезной привычкой"
    )
    frequency = models.PositiveSmallIntegerField(
        default=1,
        help_text="Периодичность выполнения привычки для напоминания в днях."
    )
    reward = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text="Вознаграждение после выполнения привычки."
    )
    duration = models.PositiveIntegerField(
        help_text="Время, которое предположительно потратит пользователь на выполнение привычки в секундах."
    )
    is_public = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action} at {self.time} in {self.place}"
