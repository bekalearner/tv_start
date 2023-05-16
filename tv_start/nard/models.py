from django.db import models


class Tournament(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Турнир нарды"
        verbose_name_plural = "Турниры нарды"


class Backgammon(models.Model):
    name = models.CharField()
    url = models.URLField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    match_date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='nard_images/', null=True, default='nard_images/nardy-youtube-13_03_23-600x350.jpg')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Матч нарды"
        verbose_name_plural = "Матчи нарды"
