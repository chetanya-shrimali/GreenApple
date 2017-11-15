from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.urls import reverse

from order.models import Dish, Order
from menu.models import SubMenu
from order.forms import Order, HomeForm, PickUpForm


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

def add_order(request, pk1, pk2):
    # sub_menu_model = apps.get_model('menu.SubMenu')
    add_sub_menu = SubMenu.objects.get(pk=pk1)

    dish_name = add_sub_menu.dish_name
    dish_price = add_sub_menu.price
    order_list = Order.objects.get(pk=pk2)
    print(dish_price)
    print(dish_name)
    print(order_list.id)

    dish = Dish.objects.create(name=dish_name, price=dish_price)
    dish.order.add(Order.objects.get(pk=pk2))
    dish.save()

    return redirect('/order/')


def home_delivery(request):
    if request.method == 'POST':
        home_form = HomeForm(request.POST)

        if home_form.is_valid():
            homes = home_form.save(commit=False)
            # name = home_form.cleaned_data['name']
            # email = home_form.cleaned_data['email']
            homes.save()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            print(home_form.errors)

    else:
        home_form = HomeForm()

    return render(request, 'order/order_details.html',
                  {'home_form': home_form})


def pick_up(request):
    if request.method == 'POST':
        pick_form = PickUpForm(request.POST)

        if pick_form.is_valid():
            homes = pick_form.save(commit=False)
            # name = home_form.cleaned_data['name']
            # email = home_form.cleaned_data['email']
            homes.save()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            print(pick_form.errors)

    else:
        pick_form = PickUpForm()

    return render(request, 'order/order_details.html',
                  {'pick_form': pick_form})
