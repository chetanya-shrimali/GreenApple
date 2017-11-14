from django.shortcuts import render


def order(request):
    return render(request, 'order/order.html')

def order_details(request):
    return render(request, 'order/order_details.html')