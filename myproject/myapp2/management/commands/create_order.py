from django.core.management.base import BaseCommand

from myapp2.models import Order



class Command(BaseCommand):
    help = "Create order."
    def handle(self, *args, **kwargs):
        order = Order(client_id=3, total_amount=3)
        order.save()
        order.products.add(1)
        order.products.add(2)
        order.products.add(3)
        self.stdout.write(f'{order}')
