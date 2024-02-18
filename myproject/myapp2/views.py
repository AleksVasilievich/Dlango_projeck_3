from django.shortcuts import render
from django.http import HttpResponse
import logging

logging.basicConfig(filename='app.log', level=logging.INFO)

def index2(request):
    html = """
        <html>
        <head>
            <title>Страница myapp2</title>
        </head>
        <body>
            <h1>Добро пожаловать на страницу myapp2</h1>
            <p>Здесь вы найдете много интересного контента.</p>
        </body>
        </html>
        """
    log_data = "Посещена страница myapp2"
    logging.info(log_data)

    return HttpResponse(html)
