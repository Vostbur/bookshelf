from django.contrib import admin

from .models import (
    Reader,
    Book
)


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'get_readers_str')

    def get_readers_str(self, obj):
        return ', '.join(obj.readers.all().values_list('name', flat=True))
    get_readers_str.short_description = "Читатели"


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book, BookAdmin)
