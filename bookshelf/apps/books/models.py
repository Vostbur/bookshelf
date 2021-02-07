from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now
    )

    def __str__(self):
        return self.title
