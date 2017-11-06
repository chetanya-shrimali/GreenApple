from book_a_table.forms import BookForm
from django.apps import apps
from django.shortcuts import render
from django.views import View


# def book(request):
#     return render(request, 'book_a_table/reservations.html')


class BookFormView(View):
    form_class = BookForm
    template_name = 'book_a_table/reservations.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'book_a_table/reservations.html',
                      {'form': form})

    def post(self):
        pass


class CustomerFormView(View):
    form_class = apps.get_model('order.Customer')
    template_name = 'book_a_table/customer_registration.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request,
                      'book_a_table/../order/templates/order/customer_registration.html',
                      {'form': form})

    def post(self):
        pass
