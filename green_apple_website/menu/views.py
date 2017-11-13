from django.shortcuts import render

from .models import Menu, SubMenu


def menu(request):
    all_menu = Menu.objects.all()
    return render(request, 'menu/menu.html', {'all_menu': all_menu})


def sub_menu(request, pk):
    all_sub_menu = SubMenu.objects.filter(menu=pk)
    # all_sub_menu = get_object_or_404(SubMenu, pk=pk)
    return render(request, 'menu/sub_menu.html',
                  {'all_sub_menu': all_sub_menu})
