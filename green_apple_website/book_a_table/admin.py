from book_a_table.models import BookDetail
from django.contrib import admin


class BookDetailAdmin(admin.ModelAdmin):
    list_display = ('customer', 'contact', 'email', 'total_persons', 'date', 'time')


admin.site.register(BookDetail, BookDetailAdmin)
