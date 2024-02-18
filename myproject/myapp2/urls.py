from django.urls import path
from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', views.index2, name='index2'),
    path('client_orders/<int:client_id>/', views.client_orders, name='client_orders'),
    # path('admin/', admin.site.urls),

]