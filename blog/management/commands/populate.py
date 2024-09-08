# management/commands/populate.py
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Post


class Command(BaseCommand):
    help = 'Populates the database with fake posts'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Post.objects.create(
                title=fake.sentence(),
                content=fake.text(),
                category_id=1
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the database with fake posts!'))
