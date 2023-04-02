from django.db import models


class Author(models.Model):
    email = models.EmailField("почта", blank=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "адресант"
        verbose_name_plural = "адресанты"


class Feedback(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Получено"
        IN_PROGRESS = "in progress", "В обработке"
        COMPLETED = "completed", "Ответ дан"

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField("содержание", blank=False)
    created_on = models.DateTimeField("создано", auto_now_add=True)
    status = models.CharField(
        "статус",
        choices=Status.choices,
        max_length=11,
        default=Status.PENDING,
        blank=False,
    )

    def __str__(self):
        return f"Сообщение от {self.author.email}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
