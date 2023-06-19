from django.db import models


class Services(models.Model):
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    img = models.ImageField(upload_to='services_img', blank=True)

    def __str__(self):
        return f'{self.subtitle} --- {self.title}'
