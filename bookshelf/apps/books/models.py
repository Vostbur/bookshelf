from django.db import models
from django.utils import timezone


class Reader(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(
        verbose_name='created at',
        default=timezone.now
    )
    readers = models.ManyToManyField(Reader)

    class Meta:
        ordering = ['id']
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
