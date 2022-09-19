from email.policy import default
from random import choices
from django.db import models

class MywatchlistItem(models.Model):
    WATCHED_CHOICES = (
      ("Sudah ditonton","watched"),
      ("Belum ditonton","not_watched"),
    )

    RATING_CHOICES = (
      (5, "very good"),
      (4, "good"),
      (3, "mediocre"),
      (2, "bad"),
      (1, "very bad")
    )
    watched = models.CharField(max_length=50,choices=WATCHED_CHOICES, default="not_watched")
    title  = models.CharField(max_length=255)
    rating  = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    release_date  = models.DateField()
    review  = models.TextField()