from django.db import models

class SportType(models.Model):
    name = models.CharField(max_length=100)
    logo = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    logo = models.URLField(blank=True)
    # sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE, related_name='sport_type')
    def __str__(self):
        return self.name

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

class Match(models.Model):
    url = models.URLField(blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one',blank=False)
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two',blank=False)
    sport_type = models.ForeignKey(SportType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.team_one} vs {self.team_two}"