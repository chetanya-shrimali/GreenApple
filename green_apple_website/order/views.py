from django.http import HttpResponse
from django.shortcuts import render
from django.apps import apps
from order.models import Dish


def order(request):
    menu_model = apps.get_model('menu.Menu')
    sub_menu_model = apps.get_model('menu.SubMenu')
    all_menu = menu_model.objects.all()
    all_sub_menu = sub_menu_model.objects.all()
    return render(request, 'order/order.html',
                  {'all_menu': all_menu, 'all_sub_menu': all_sub_menu})


def order_details(request):
    return render(request, 'order/order_details.html')


def add_order_details(request, pk):
    menu_model = apps.get_model('menu.Menu')
    sub_menu_model = apps.get_model('menu.SubMenu')
    add_sub_menu = sub_menu_model.objects.get(pk=pk)
    print(add_sub_menu.dish_name)
    print(add_sub_menu.price)
    name = add_sub_menu.dish_name
    price = add_sub_menu.price
    dish = Dish(name=name, price=price, order=pk)
    dish.save()
    return HttpResponse("added")
