from datetime import date
from email.policy import default
from django.db import models
from django.conf import settings


class TodolistItem(models.Model):
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    date = models.DateField(default=date.today)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)