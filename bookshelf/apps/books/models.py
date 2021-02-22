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


# class RankBooks(models.Model):
#     reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
#     rank = models.ForeignKey('Rank', on_delete=models.CASCADE)
#     quantity = models.PositiveSmallIntegerField(default=1)
#
#     def __str__(self):
#         return f'{self.quantity} раз {self.reader_id} поставил {self.rank_id}'
#
#
# class Rank(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     readers = models.ManyToManyField(
#         Reader,
#         through=RankBooks
#     )
#
#     def __str__(self):
#         return f'{self.id} {self.book_id}'
