from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.apps import apps
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from order.models import Dish, Order
from menu.models import SubMenu
from order.forms import Order, HomeForm, PickUpForm
from validate_email import validate_email
from django.core.mail import EmailMessage


def order(request):
    menu_model = apps.get_model('menu.Menu')
    sub_menu_model = apps.get_model('menu.SubMenu')
    all_menu = menu_model.objects.all()
    all_sub_menu = sub_menu_model.objects.all()
    return render(request, 'order/order.html',
                  {'all_menu': all_menu, 'all_sub_menu': all_sub_menu})


def order_details(request):
    return render(request, 'order/order_details.html')


def add_order(request, pk1, pk2):
    # sub_menu_model = apps.get_model('menu.SubMenu')
    add_sub_menu = SubMenu.objects.get(pk=pk1)
    menu_model = apps.get_model('menu.Menu')
    sub_menu_model = apps.get_model('menu.SubMenu')

    all_menu = menu_model.objects.all()
    all_sub_menu = sub_menu_model.objects.all()
    dish_name = add_sub_menu.dish_name

    dish_price = add_sub_menu.price
    order_list = Order.objects.get(pk=pk2)

    dish = Dish.objects.create(name=dish_name, price=dish_price)
    dish.order.add(Order.objects.get(pk=pk2))
    dish.save()

    get_dishes = Dish.objects.all()
    final_dishes = ""

    value = ""
    sum = 0
    for i in get_dishes:
        print(order_list.id)
        print(pk2)

        try:
            value = i.order.get(pk=order_list.id)
            print(value)
            print('reached')
            if value is not None:
                final_dishes = Dish.objects.filter(
                    order=i.order.get(pk=order_list.id)).all()
                print(final_dishes)
                print(value.user_email)
                for i in final_dishes:
                    sum += i.price

                break
            else:
                continue
        except Exception as e:
            continue

    return render(request, 'order/order.html',
                  {'final_dishes': final_dishes, 'all_menu': all_menu,
                   'all_sub_menu': all_sub_menu, 'order_id': pk2,
                   'value': value, 'sum': sum})


@csrf_protect
def home_delivery(request):
    if request.method == 'POST':
        home_form = HomeForm(request.POST)

        if home_form.is_valid():
            homes = home_form.save(commit=False)
            homes.save()
            print(homes.id)
            menu_model = apps.get_model('menu.Menu')
            sub_menu_model = apps.get_model('menu.SubMenu')

            all_menu = menu_model.objects.all()
            all_sub_menu = sub_menu_model.objects.all()

            return render(request, 'order/order.html', {'all_menu': all_menu,
                                                        'all_sub_menu': all_sub_menu,
                                                        'order_id': homes.id})

        else:
            print(home_form.errors)

    else:
        home_form = HomeForm()

    return render(request, 'order/order_details.html',
                  {'home_form': home_form})


@csrf_protect
def pick_up(request):
    if request.method == 'POST':
        pick_form = PickUpForm(request.POST)

        if pick_form.is_valid():
            homes = pick_form.save(commit=False)
            # name = home_form.cleaned_data['name']
            # email = home_form.cleaned_data['email']
            homes.save()
            return render(request, 'order/pickup_confirmation.html', {})
        else:
            print(pick_form.errors)

    else:
        pick_form = PickUpForm()

    return render(request, 'order/order_details.html',
                  {'pick_form': pick_form})


def mail_order(request, pk):
    user = Order.objects.get(pk=pk)
    name = user.user
    email_send = user.user_email
    number = user.phone_number

    print (number)

    email = EmailMessage('Regarding Home Delivery',
                         "Received mail from " + str(
                             email_send) + "\n\n" + "name: " +
                         str(name) + "\n" + "contact: " + str(number),
                         to=['chetanyashrimalie5@gmail.com', ])
    email.send()

    email = EmailMessage('Regarding Home Delivery',
                         "Hey " + str(
                             name) + ",\n\n" + "We have "
                                               "received "
                                               "your request "
                                               "for order "
                                               "\n" +
                         "We will contact you shortly on " + str(number),
                         to=[email_send,
                             'chetanyashrimalie5@gmail.com'],
                         reply_to=[email_send, ])
    email.send()
    print('reached')
    return render(request, 'order/order_confirmation.html', {})
