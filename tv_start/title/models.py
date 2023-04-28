from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    post_date = models.DateField(null=True)
    time = models.TimeField(null=True)
    url = models.URLField(blank=True)


    def __str__(self):
        return f'Дата создания {self.date}, дата поста {self.post_date}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"