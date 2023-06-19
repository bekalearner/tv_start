from django.db import models


class AllSiteInfo(models.Model):
    number = models.CharField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)

    def __str__(self):
        return "Site Information"