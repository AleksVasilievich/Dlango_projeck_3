from django.core.management.base import BaseCommand
from myapp2.models import Product


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            product = Product(name=f'name{i}', description=f'description{i}', price=i * 0.3, quantity=i + 10)
            product.save()
            self.stdout.write(f'{product}') # Вывод информации в консоль