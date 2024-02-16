from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)


def orders(request):
    html = """
        <html>
        <head>
            <title>Список заказанных товаров</title>
        </head>
        <body>
            <h1>Список заказанных товаров</h1>
        
            <h2>За последние 7 дней (неделю)</h2>
            <ul>
                {% for order in orders_week %}
                    <li>{{ order.client }} - {{ order.products }} - {{ order.created_at }}</li>
                {% endfor %}
            </ul>
        
            <h2>За последние 30 дней (месяц)</h2>
            <ul>
                {% for order in orders_month %}
                    <li>{{ order.client }} - {{ order.products }} - {{ order.created_at }}</li>
                {% endfor %}
            </ul>
        
            <h2>За последние 365 дней (год)</h2>
            <ul>
                {% for order in orders_year %}
                    <li>{{ order.client }} - {{ order.products }} - {{ order.created_at }}</li>
                {% endfor %}
            </ul>
        </body>
        </html>
        """
    log_data = "Посещена страница заказов"
    logging.info(log_data)

    return HttpResponse(html)
