from django.db import models

class MywatchlistItem(models.Model):
    RATING_CHOICES = (
      (5, "very good"),
      (4, "good"),
      (3, "mediocre"),
      (2, "bad"),
      (1, "very bad")
    )
    watched = models.BooleanField(default=False)
    title  = models.CharField(max_length=255)
    rating  = models.IntegerField(choices=RATING_CHOICES, null=True, blank=True)
    release_date  = models.DateField()
    review  = models.TextField(null=True, blank=True)