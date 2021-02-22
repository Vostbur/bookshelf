from django.contrib import admin
from django.db.models import Prefetch

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at', 'get_users_str')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        prefetch = Prefetch('users')
        qs = qs.prefetch_related(prefetch)
        return qs

    def get_users_str(self, obj):
        return ', '.join([r.username for r in obj.users.all()])
    get_users_str.short_description = "Читатели"


admin.site.register(Book, BookAdmin)
