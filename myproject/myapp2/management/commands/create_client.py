from django.core.management.base import BaseCommand

from myapp2.models import Client



class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        # user = Client(name='Leo', email='leo@example.com', phone_number='00000000000', address='address_leo')
        # user = Client(name='Leo1', email='leo1@example.com', phone_number='11111111111', address='address_leo1')
        # client = Client(name='Leo2', email='leo2@example.com', phone_number='22222222222', address='address_leo2')
        # client = Client(name='Leo3', email='leo3@example.com', phone_number='33333333333', address='address_leo3')
        client = Client(name='Leo5', email='leo5@example.com', phone_number='55555555555', address='address_leo5')
        client.save()
        self.stdout.write(f'{client}')