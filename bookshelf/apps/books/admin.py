from django.forms import ModelForm
from django.contrib import admin
from django.db.models import Prefetch
from django.utils.html import mark_safe

from .models import (
    Author,
    Book
)


class BooksInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fields = ['name']
    inlines = [BooksInline]


class BookAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover'].help_text = mark_safe(
            '<span style="color:red;">Изображение будет уменьшено до разрешения 165x247</span>'
        )


class BookAdmin(admin.ModelAdmin):

    form = BookAdminForm

    list_display = ('title', 'author', 'created_at', 'get_users_str', 'image_tag')

    def get_queryset(self, request):
        qs = super().get_queryset(request).select_related('author')
        prefetch = Prefetch('users')
        qs = qs.prefetch_related(prefetch)
        return qs

    def get_users_str(self, obj):
        return ', '.join([r.username for r in obj.users.all()])

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.cover.url}" width="88" height="131" />')

    get_users_str.short_description = 'Читатели'
    image_tag.short_description = 'Обложка'


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
