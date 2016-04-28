
from invoke import run, task


@task
def runserver():
    run("python manage.py")


@task
def migrate():
    run("alembic upgrade head")


@task
def revision(msg):
    if not msg:
        print("Message is required!")
        return 
    run("alembic revision -m '{}'".format(msg))
