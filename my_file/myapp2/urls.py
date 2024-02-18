from django.urls import path

from . import views
from .views import OrderList, test1, GetOrderList, client_orders
# from .views import my_view, OrderList, OrderListView
# from .views import HelloView

app_name = 'myapp2'

urlpatterns = [
    path('', views.index, name='index0'),
    path('order/', OrderList.as_view(), name='index'),
    # path('hello/', HelloView.as_view(), name='hello'),
    # path('les2/', my_view, name='index2'),
    # path('orders/', OrderListView.as_view(), name='index4'),
    path('test1/', test1, name='index2'),
    # path('days/', client_orders, name='index5'),
    path('get/', GetOrderList.as_view(), name='index6'),
    path('days/', client_orders, name='client_orders'),
]



# path('order_detail/<int:order_id>/', DetailOrder.as_view(), name='order_detail'),