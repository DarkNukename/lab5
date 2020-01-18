
from .celery import app

from celery import Task
from requests.exceptions import RequestException

@app.task(autoretry_for=(RequestException,), retry_kwargs={'max_retries': 5}, retry_backoff=True)
def post(payload: dict):
    pass


@app.task(autoretry_for=(RequestException,), retry_kwargs={'max_retries': 5}, retry_backoff=True)
def patch(payload: dict):
    pass


@app.task(autoretry_for=(RequestException,), retry_kwargs={'max_retries': 5}, retry_backoff=True)
def delete(payload: dict):
    pass