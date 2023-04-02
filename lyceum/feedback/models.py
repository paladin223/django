from django.db import models


class Author(models.Model):
    email = models.EmailField("почта", blank=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "адресант"
        verbose_name_plural = "адресанты"


class Feedback(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    text = models.TextField("содержание", blank=False)
    created_on = models.DateTimeField("создано", auto_now_add=True)
    status = models.CharField(
        "статус",
        max_length=11,
        blank=False,
    )

    def __str__(self):
        return f"Сообщение от {self.author.email}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"
