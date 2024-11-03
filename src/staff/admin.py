from django.contrib import admin
from django.utils.html import format_html

from staff.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('fio', ),
    }
    list_display = (
        'fio',
        'stage',
        'published',
        'view_image',
    )
    list_filter = (
        'stage',
        'published',
        'roles',
    )

    def view_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 100px; height: 75px;" />',
                obj.image.url,
            )
        return "Нет изображения"

    view_image.short_description = 'Фото'
