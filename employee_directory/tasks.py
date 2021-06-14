import random
from celery import shared_task

from .models import Employee


@shared_task
def pay_wages():
    employees = Employee.objects.values_list('id', flat=True)
    random_id = random.choices(employees)
    random_employee = Employee.objects.filter(id__in=random_id)

    for data_random_employee in random_employee:
        salary_id = data_random_employee.salary
        paid_salary = data_random_employee.paid_salary
        data_random_employee.paid_salary = salary_id + paid_salary
        data_random_employee.save()
        return f'{data_random_employee} начисленно :{data_random_employee.salary}'


@shared_task
def delete_salary_paid():
    employee = Employee.objects.all()
    employee.update(paid_salary=0)
