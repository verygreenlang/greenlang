from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = settings.DJANGO_SU_EMAIL
        user_password = settings.DJANGO_SU_PASSWORD

        if not User.objects.filter(email=user).exists():
            User.objects.create_superuser(user, user_password)
