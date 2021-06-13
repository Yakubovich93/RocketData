from django.contrib import admin

from .models import Employee
from .tasks import delete_salary_paid


def delete_paid_salary(modeladmin, request, queryset):
    if queryset.count() > 2:
        delete_salary_paid.delay()
    else:
        queryset.update(paid_salary=0)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'salary', 'paid_salary', 'parent')
    list_filter = ('position', 'level')
    ordering = ['level']
    actions = [delete_paid_salary]
