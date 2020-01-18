from celery import Celery

app = Celery(
    'MyQueue',
    broker = 'redis://localhost:6379/0',
    include = ['celeryQue.tasks']
)

if __name__ == "__main__":
    app.start()