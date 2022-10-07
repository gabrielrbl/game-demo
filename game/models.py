from django.db import models

from player.models import Player


class Game(models.Model):
    date = models.DateField()
    players = models.ManyToManyField(Player)

    def __str__(self):
        return f"{self.pk} - {self.date}"
