from __future__ import absolute_import, unicode_literals
from try_celery.celery import app


@app.task
def add():
    for i in range(1, 1000):
        print('{}. Charles'.format(i))


@app.task
def mul(x, y):
    return x * y
