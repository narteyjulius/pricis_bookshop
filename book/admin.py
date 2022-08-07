from django.contrib import admin
from .models import Book


# @admin.register(Category)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'available')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    list_filter = ('status', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
#     raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

# class ReviewInline(admin.TabularInline):
#     model = Review

# class BookAdmin(admin.ModelAdmin):
# #     inlines =[ReviewInline]
#     list_display = ("title", "author", "price",)

# admin.site.register(Book, BookAdmin)