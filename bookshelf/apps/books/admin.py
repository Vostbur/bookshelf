from django.contrib import admin
from django.db.models import Prefetch

from .models import (
    Reader,
    Book,
    # RankBooks,
    # Rank
)


class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'get_readers_str')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        prefetch = Prefetch('readers')
        qs = qs.prefetch_related(prefetch)
        return qs

    def get_readers_str(self, obj):
        return ', '.join([r.name for r in obj.readers.all()])
    get_readers_str.short_description = "Читатели"


# class RankBooksAdmin(admin.ModelAdmin):
#     pass
#
#
# class RankAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Reader, ReaderAdmin)
admin.site.register(Book, BookAdmin)
# admin.site.register(RankBooks, RankBooksAdmin)
# admin.site.register(Rank, RankAdmin)
