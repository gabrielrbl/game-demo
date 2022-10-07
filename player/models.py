from django.db import models
from django.contrib.auth.models import User


class PlayerBoard(models.Model):
    points = models.IntegerField()

    def __str__(self):
        return str(self.points)


class Player(models.Model):
    user = models.ForeignKey(
        User, related_name="players", on_delete=models.CASCADE
    )
    picture = models.ImageField(default="default.png")
    GENDER_MALE = "M"
    GENDER_FEMALE = "F"
    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birthday = models.DateField()
    motto = models.TextField()
    board = models.ForeignKey(
        PlayerBoard, related_name="players", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}"
