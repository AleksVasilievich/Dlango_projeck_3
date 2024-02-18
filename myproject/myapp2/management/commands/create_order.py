from django.core.management.base import BaseCommand
from myapp2.models import Order

#

class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        order = Order(client='client', total_amount='total_amount')
        order.save()
        self.stdout.write(f'{order}') # Вывод информации в консоль



# def create_order(client, products, total_amount):
#     new_order = Order(client=client, total_amount=total_amount)
#     new_order.save()
#     new_order.products.add(*products)
#     return new_order