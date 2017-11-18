from django.contrib import admin

from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'note')


admin.site.register(Note, NoteAdmin)
