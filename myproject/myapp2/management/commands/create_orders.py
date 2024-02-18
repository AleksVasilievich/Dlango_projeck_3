from django.core.management.base import BaseCommand
from myapp2.models import Order, Client


class Command(BaseCommand):
    help = "Creating orders for clients"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()  # Получение всех клиентов из базы данных
        for client in clients:
            for i in range(1, 11):
                order = Order(client=client, total_amount=i * 100)  # Использование клиента из списка
                order.save()
                self.stdout.write(f'Order for {client.name} created')


# class Command(BaseCommand):
#     help = "Create orders."
#     def handle(self, *args, **kwargs):
#         client_name = 'client'  # Здесь вы можете уточнить имя клиента
#         for i in range(1, 11):
#             order = Order(client=client_name, total_amount=i * 100)
#             order.save()
#             self.stdout.write(f'{order}') # Вывод информации в консоль