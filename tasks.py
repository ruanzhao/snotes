
from invoke import run, task

@task
def runserver():
    run("python manage.py")

@task
def migrate():
    run("alembic upgrade head")
