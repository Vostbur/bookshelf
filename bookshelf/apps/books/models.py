from django.db import models
from django.utils import timezone

from apps.users.models import User


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now
    )
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
