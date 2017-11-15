from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from order.models import Dish, Order
from menu.models import SubMenu


def order(request):
    menu_model = apps.get_model('menu.Menu')
    sub_menu_model = apps.get_model('menu.SubMenu')
    all_menu = menu_model.objects.all()
    all_sub_menu = sub_menu_model.objects.all()
    return render(request, 'order/order.html',
                  {'all_menu': all_menu, 'all_sub_menu': all_sub_menu})


def order_details(request):
    return render(request, 'order/order_details.html')


# def add_order_details(request, pk):
#     menu_model = apps.get_model('menu.Menu')
#     sub_menu_model = apps.get_model('menu.SubMenu')
#     add_sub_menu = sub_menu_model.objects.get(pk=pk)
#
#     print(add_sub_menu.dish_name)
#     print(add_sub_menu.price)
#     name = add_sub_menu.dish_name
#     price = add_sub_menu.price
#     dish = Dish(name=name, order=Order.objects.get(pk=pk))
#
#     return HttpResponse("added")

def add_order(request, pk):
    # sub_menu_model = apps.get_model('menu.SubMenu')
    add_sub_menu = SubMenu.objects.get(pk=pk)

    dish_name = add_sub_menu.dish_name
    dish_price = add_sub_menu.price

    print(dish_price)
    print(dish_name)
    # order_m = get_object_or_404(sub_menu_model, pk=pk)
    order_list = Order.objects.get(pk=pk)

    Dish(dish_name, dish_price, order_list).save()

    return HttpResponse("added")
