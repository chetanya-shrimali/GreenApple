from django.shortcuts import render
from django.views import generic
from menu.models import *


def order(request):
    return render(request, 'order/order.html')


def order_details(request):
    return render(request, 'order/order_details.html')


class OrderListView(generic.ListView):
    model = Menu
    template_name = 'order/order.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return Menu.objects.all()


def order_sub_list(request, pk):
    sub_list = SubMenu.objects.filter(pk=pk)
