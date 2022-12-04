from django.contrib import admin
from contacts.models import Contact, Number


class NumberInlineAdmin(admin.TabularInline):
    model = Number


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'primary_number')
    inlines = [NumberInlineAdmin]
