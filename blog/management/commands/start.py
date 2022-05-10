import datetime
import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post


class Command(BaseCommand):
    help = 'Start script'

    def handle(self, *args, **kwargs):
        if User.objects.count() > 0:
            self.stdout.write(self.style.SUCCESS('NO ACTIONS NEEDED'))
        else:
            for i in range(15):
                User.objects.create_user(
                    username=f'user{i + 1}',
                    password='123',
                    is_staff=True if i % 2 == 0 else False
                )
            User.objects.create_superuser(
                username='admin',
                password='123'
            )

            users = User.objects.all()

            for i in range(200):
                new_post = Post.objects.create(
                    title=f'Post number {i + 1}',
                    date=datetime.date(2022, 5, random.randint(1, 15)),
                    author=random.choice(users)
                )
                for like in range(random.randint(1, 3)):
                    new_post.likes.add(random.choice(users))
            self.stdout.write(self.style.SUCCESS('ALL DONE, OK'))
