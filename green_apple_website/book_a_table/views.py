from book_a_table.forms import BookForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
# from django.apps import apps
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect


# def book(request):
#     return render(request, 'book_a_table/reservations.html')


# class BookFormView(View):
#     form_class = BookForm
#     template_name = 'book_a_table/reservations.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request, 'book_a_table/reservations.html',
#                       {'form': form})
#
#     def post(self):
#         pass
#
#
# class CustomerFormView(View):
#     form_class = apps.get_model('order.Customer')
#     template_name = 'book_a_table/customer_registration.html'
#
#     def get(self, request):
#         form = self.form_class(None)
#         return render(request,
#                       'book_a_table/../order/templates/order/customer_registration.html',
#                       {'form': form})
#
#     def post(self):
#         pass


@csrf_protect
def book_table(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            table = book_form.save()
            table.save()
            return HttpResponseRedirect(reverse('home:index'))
        else:
            print(book_form.errors)
            return HttpResponseRedirect(reverse('home:index'))
    else:
        book_form = BookForm()

    return render(request, 'book_a_table/reservations.html', {'book_form': book_form})
