from django.db import models
from django.utils import timezone
class Article(models.Model):
    title = models.CharField(max_length=200)
    title_live = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)
    post_date = models.DateField(null=True)
    time = models.TimeField(null=True)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"