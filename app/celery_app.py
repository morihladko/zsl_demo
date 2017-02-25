from celery import Celery

from zsl.interface.importer import initialize_web_application
initialize_web_application()

from zsl.application.service_application import service_application

from zsl.interface.celery.worker import CeleryTaskQueueOutsideWorkerModule

service_application.add_injector_module(CeleryTaskQueueOutsideWorkerModule)

app = Celery(backend='rpc', broker='redis://localhost')
