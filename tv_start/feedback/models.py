from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'