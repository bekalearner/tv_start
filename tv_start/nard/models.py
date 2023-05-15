from django.db import models


class SportType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='nard_images/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Нарды иконка"
        verbose_name_plural = "Нарды иконка"


class Tournament(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Турнир нарды"
        verbose_name_plural = "Турниры нарды"


class Backgammon(models.Model):
    name = models.CharField(null=True, blank=True)
    url = models.URLField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    match_date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='nard_images/')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Матч нарды"
        verbose_name_plural = "Матчи нарды"
