from django.db import models
from django.utils import timezone

from apps.users.models import User

from django_resized import ResizedImageField


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Автор')

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        default=timezone.now
    )
    cover = ResizedImageField(size=[165, 247], upload_to='covers', default='default.jpg')
    users = models.ManyToManyField(User)

    class Meta:
        ordering = ['title', 'author']
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title
