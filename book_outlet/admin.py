from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    pass


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name",)
    list_display = ("first_name", "last_name",)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("author", "rating",)
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Country)
