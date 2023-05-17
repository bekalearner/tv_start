from django.db import models

class SportType(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='sport_type_logo/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Спорт"
        verbose_name_plural = "Спорт"

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to='team_logo/')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Tournament(models.Model):
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, blank=True)
    name = models.CharField()
    GENDER_CHOICES = (
        ('м', 'Мужской'),
        ('ж', 'Женский'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    def __str__(self):
        return f"{self.sport_type}   {self.name}   {self.gender}"

    class Meta:
        verbose_name = "Турнир"
        verbose_name_plural = "Турниры"

class Match(models.Model):
    url = models.URLField(blank=True)
    created_date = models.DateField(auto_now_add=True, null=True)
    match_date = models.DateField(null=True)
    time = models.TimeField(null=True)
    image = models.ImageField(upload_to='match_images/')
    youtube_video_url = models.URLField(blank=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one',blank=False)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two',blank=False)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_one} vs {self.team_two}"

    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"