import random

from django.core.management.base import BaseCommand

from apps.books.models import Book
from apps.users.models import User

from faker import Faker


class Command(BaseCommand):

    def generate(self, amount=10):
        fake = Faker('ru_RU')

        users = list(User.objects.values_list('id', flat=True))
        for i in range(amount):
            book = Book.objects.create(
                title=fake.text(max_nb_chars=50),
                author=fake.name(),
                created_at=fake.date_time()
            )
            book.users.add(
                *random.sample(
                    users, random.randint(1, len(users))
                )
            )

    def handle(self, *args, **options):
        self.generate()
