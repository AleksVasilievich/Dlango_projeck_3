from django.core.management.base import BaseCommand

# from semfirst.myapp2.models import User
from myapp2.models import Product



class Command(BaseCommand):
    help = "Create product."
    def handle(self, *args, **kwargs):
        # product = Product(name='апельсины', description='из Турции', price=23.0, quantity=10.0)
        # product = Product(name='мандарины', description='из Абхазии', price=34.0, quantity=11)
        # product = Product(name='яблоки', description='белый налив', price=28.0, quantity=12)
        # product = Product(name='огурцы', description='зелёные', price=55.0, quantity=13)
        product = Product(name='малина', description='садовая', price=70, quantity=14)
        product.save()
        self.stdout.write(f'{product}')

