import os

from celery import Celery, shared_task
from celery.schedules import crontab 


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'init_app.settings')

app = Celery('init_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'new_game': {
        'task': 'my_app.tasks.new_game',
        'schedule': crontab()  
    },

    'new_vendors': {
        'task': 'my_app.tasks.new_vendor',
        'schedule' : crontab(0, '*', '*', '*', '*')
    },

    'new_categories': {
        'task': 'my_app.tasks.new_categories',
        'schedule' : crontab(5, '*', '*', '*', '*')
        
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
