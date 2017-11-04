from book_a_table.forms import BookForm
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
    form_class = BookForm
    template_name = 'book_a_table/reservations.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'book_a_table/reservations.html',
                      {'form': form})

    def post(self):
        pass
