from django.core.management.base import BaseCommand
from myapp2.models import Client


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        for i in range(15):
            client = Client(name=f"name{i}", email=f"email{i}", phone_number=f"phone_number{i}", address=f"address{i}")
            client.save()
            self.stdout.write(f'{client}')  # Вывод информации в консоль
