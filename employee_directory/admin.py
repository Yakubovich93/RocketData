from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Employee
from .tasks import delete_salary_paid


def delete_paid_salary(modeladmin, request, queryset):
    if queryset.count() > 2:
        delete_salary_paid.delay()
    else:
        queryset.update(paid_salary=0)


def link_to_boss(field_name):
    def _link_to_boss(obj):
        linked_obj = getattr(obj, field_name)
        if linked_obj is None:
            return 'сам себе Босс'
        app_label = linked_obj._meta.app_label
        model_name = linked_obj._meta.model_name
        view_name = f'admin:{app_label}_{model_name}_change'
        link_url = reverse(view_name, args=[linked_obj.pk])
        return format_html('<a href="{}">{}</a>', link_url, linked_obj)

    _link_to_boss.short_description = 'Босс'
    return _link_to_boss


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'paid_salary', link_to_boss(field_name='parent'))
    list_filter = ('position', 'level')
    ordering = ['level']
    actions = [delete_paid_salary]
