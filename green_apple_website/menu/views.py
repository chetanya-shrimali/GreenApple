from django.shortcuts import render

from .models import SubMenu, Menu


def menu(request):
    all_menu = Menu.objects.all()
    return render(request, 'menu/menu.html', {'all_menu': all_menu})


def sub_menu(request, pk):
    all_sub_menu = SubMenu.objects.filter(menu=pk)
    return render(request, 'menu/sub_menu.html',
                  {'all_sub_menu': all_sub_menu})
