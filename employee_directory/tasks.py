import random
from celery import shared_task

from .models import Employee


@shared_task
def pay_wages():
    employees = Employee.objects.all().order_by()
    first_id = employees.first().id
    last_id = employees.last().id
    random_id = random.randint(first_id, last_id)
    employee_id = Employee.objects.filter(id=random_id)

    for data_employee_id in employee_id:
        salary_id = data_employee_id.salary
        paid_salary = data_employee_id.paid_salary
        data_employee_id.paid_salary = salary_id + paid_salary
        data_employee_id.save()
        return f'{data_employee_id} начисленно :{data_employee_id.salary}'


@shared_task
def delete_salary_paid():
    employee = Employee.objects.all()
    employee.update(paid_salary=0)
