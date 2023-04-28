from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name