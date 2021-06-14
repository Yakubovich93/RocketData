from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
import mptt


class Employee(MPTTModel):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    EMPLOYEE_TYPE = (
        ('МАСТЕР', 'мастер'),
        ('ПРОРАБ', 'прораб'),
        ('НАЧАЛЬНИК УЧАСТКА', 'начальник участка'),
        ('ГЛАНЫЙ ИНЖЕНЕР', 'главный инженер'),
        ('ДИРЕКТОР', 'директор'),
    )

    name = models.CharField(verbose_name='ФИО', max_length=256)
    position = models.CharField(verbose_name='Должность', max_length=100, choices=EMPLOYEE_TYPE,
                                default=EMPLOYEE_TYPE[0][0])
    employment_date = models.DateTimeField(verbose_name='Дата приема на работу', auto_now=True)
    salary = models.DecimalField(verbose_name='Заработная плата', decimal_places=2, max_digits=8,
                                 validators=[MinValueValidator(Decimal('0'))], null=True, blank=True)
    paid_salary = models.DecimalField(verbose_name='Выплаченная зарплата', decimal_places=2, max_digits=10,
                                      validators=[MinValueValidator(Decimal('0'))], null=True, blank=True, default=0)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Босс')

    def __str__(self):
        return f'{self.name} [{self.position}]'


mptt.register(Employee)
