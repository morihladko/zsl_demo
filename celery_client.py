from celery import Celery

from zsl.interface.importer import initialize_web_application

initialize_web_application()

app = Celery('zsl', backend='rpc', broker='redis://localhost')

from zsl.interface.celery.worker import zsl_task
r = zsl_task.delay({'path': 'hello_world_task', 'data':{}}).get()

print(r)
