from django.contrib import admin
from .models import Author, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    max_num = 10
    fields = ('title', 'published_year', 'status', 'cover')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birth_year',
        'books_count',
    )
    search_fields = ('first_name', 'last_name')
    inlines = [BookInline]

    def books_count(self, obj):
        return obj.books.count()

    books_count.short_description = 'Кількість книг'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'published_year',
        'status',
        'is_big_book',
    )

    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('status', 'author')

    readonly_fields = ('created_at',)

    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'author', 'cover')
        }),
        ('Опис', {
            'fields': ('description',)
        }),
        ('Деталі', {
            'fields': ('published_year', 'pages')
        }),
        ('Стан', {
            'fields': ('status',)
        }),
        ('Метадані', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    actions = ['make_available', 'make_archived']

    def is_big_book(self, obj):
        return obj.pages > 500

    is_big_book.boolean = True
    is_big_book.short_description = 'Велика книга'

    def make_available(self, request, queryset):
        updated = queryset.update(status='available')
        self.message_user(
            request,
            f'Оновлено {updated} книг — тепер доступні.'
        )

    def make_archived(self, request, queryset):
        updated = queryset.update(status='archived')
        self.message_user(
            request,
            f'{updated} книг архівовано.'
        )
