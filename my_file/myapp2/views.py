from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Order
from django.views.generic import TemplateView

import logging
logging.basicConfig(filename='app.log', level=logging.INFO)


# class OrderList(View):
#     def get(self, request):
#         orders_week = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=7))
#         orders_month = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=30))
#         orders_year = Order.objects.filter(created_at__gte=timezone.now() - timedelta(days=365))
#         return render(request, 'order_list.html', {'orders_week': orders_week, 'orders_month': orders_month, 'orders_year': orders_year})
#
# class DetailOrder(View):
#     def get(self, request, order_id):
#         order = get_object_or_404(Order, pk=order_id)
#         return render(request, 'order_detail.html', {'order': order})


from django.views.generic import TemplateView, ListView
from .models import Order, Product, Client
from django.utils import timezone
from datetime import timedelta

import logging
logging.basicConfig(filename='app.log', level=logging.INFO)

from django.shortcuts import render
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product


# Create your views here.
def index(request):
    return render(request, 'myapp2/index0.html')


def client_orders(request, client_id):
    client = Client.objects.get(pk=client_id)

# def client_orders(request, myapp2_client_id):
#     client = Client.objects.get(pk=myapp2_client_id)

    # За последние 7 дней
    last_7_days = timezone.now() - timedelta(days=7)
    client_orders_last_7_days = Product.objects.filter(order__client=client,
                                                       order__order_date__gte=last_7_days).distinct()

    # За последние 30 дней
    last_30_days = timezone.now() - timedelta(days=30)
    client_orders_last_30_days = Product.objects.filter(order__client=client,
                                                        order__order_date__gte=last_30_days).distinct()

    # За последние 365 дней
    last_365_days = timezone.now() - timedelta(days=365)
    client_orders_last_365_days = Product.objects.filter(order__client=client,
                                                         order__order_date__gte=last_365_days).distinct()

    return render(request, 'myapp2/index7.html', {
        'client_orders_last_7_days': client_orders_last_7_days,
        'client_orders_last_30_days': client_orders_last_30_days,
        'client_orders_last_365_days': client_orders_last_365_days,
    })


# def client_orders(request):
#     orders_week = Product.objects.filter(order_date__gte=timezone.now() - timedelta(days=7)).distinct()



    # client = Client.objects.get(pk=client_id)

    # orders_week = Product.objects.filter(order_date__gte=timezone.now() - timedelta(days=7)).distinct()
    # orders_month = Product.objects.filter(order_date__gte=timezone.now() - timedelta(days=30)).distinct()
    # orders_year = Product.objects.filter(order_date__gte=timezone.now() - timedelta(days=365)).distinct()
    # return render(request, 'myapp2/index.html',
    #               {'orders_week': orders_week,
    #                'orders_month': orders_month,
    #                'orders_year': orders_year})

def test1(request):
    goals = Order.objects
    test1 = {"goals": list(goals.values())}
    # return JsonResponse(data)
    # test1 = Order.client
    return render(request, "myapp2/index2.html", {'test1': test1})

class GetOrderList(View):
    def get_order(self, request):
        orders_week = JsonResponse(
            {'orders_week': list((Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7))).values())})
        orders_month = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=30))
        orders_year = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=365))

        return render(request, 'myapp2/index6.html', orders_week)


    # return (JsonResponse({'orders_week': list(orders_week.values()),
    #                         'orders_month': list(orders_month.values()),
    #                         'orders_year': list(orders_year.values())}))


class OrderList(View):
    # template_name = "myapp2/index.html"
    def get(self, request):
        # orders_week = JsonResponse(
        #     {'orders_week': list((Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7))).values())})
        orders_week = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7)).distinct()
        orders_month = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=30)).distinct()
        orders_year = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=365)).distinct()
        return render(request, 'myapp2/index.html',
                      {'orders_week': orders_week,
                       'orders_month': orders_month,
                       'orders_year': orders_year})

        # return render(request, 'myapp2/index.html',
        #             JsonResponse({'orders_week': list(orders_week.values()),
        #                         'orders_month': list(orders_month.values()),
        #                         'orders_year': list(orders_year.values())}))

    # def __str__(self):
    #     self.get(self.request)

# def client_orders(request, days):
#     end_date = timezone.now()
#     start_date = end_date - timedelta(days=days)
#     orders = Order.objects.filter(client=request.user.client, order_date__range=(start_date, end_date))
#     products = Product.objects.filter(order__in=orders).distinct().order_by('added_date')  # Получить товары из заказов клиента за указанный период
#     return render(request, 'client_orders.html', {'products': products, 'days': days})




# class OrderList(TemplateView):
#     template_name = "myapp2/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         orders_week = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=7))
#         orders_month = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=30))
#         orders_year = Order.objects.filter(order_date__gte=timezone.now() - timedelta(days=365))
#         context['orders_week'] = orders_week
#         context['orders_month'] = orders_month
#         context['orders_year'] = orders_year
#         return context


# class OrderListView(ListView):
#     model = Order  # Указываем модель, из которой будем получать данные
#     template_name = 'meapp2/index4.html'  # Указываем имя шаблона, в котором будем отображать заказы
#     context_object_name = 'orders'  # Указываем имя переменной контекста для передачи заказов в шаблон
#
#     def get_queryset(self):
#         return Order.objects.all()  # Получаем все заказы из базы данных

# class HelloView(View):
#     def get(self, request):
#         return HttpResponse("Hello World from class!")
#
# def my_view(request):
#     context = {"name": "John"}
#     return render(request, "myapp2/index2.html", context)