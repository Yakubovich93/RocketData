from django.contrib import admin

from .models import Employee


def delete_paid_salary(modeladmin, request, queryset):
    queryset.update(paid_salary=None)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'paid_salary', 'parent')
    list_filter = ('position', 'level')
    ordering = ['level']
    actions = [delete_paid_salary]
