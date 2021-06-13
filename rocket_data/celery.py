import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rocket_data.settings')

app = Celery('rocket_data')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'pay_wages_employee': {
        'task': 'employee_directory.tasks.pay_wages',
        'schedule': 10.0,
    }
}
