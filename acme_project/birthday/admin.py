from django.contrib import admin

from .models import Birthday


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    search_fields = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_filter = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_display_links = ('first_name',)


admin.site.register(Birthday, BirthdayAdmin)
