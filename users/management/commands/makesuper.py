from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()

        qs = User.objects.filter(username='admin')
        if not qs.exists():
            User.objects.create_superuser(
                'admin',
                'admin@gmail.com',
                'test12345',
            )



