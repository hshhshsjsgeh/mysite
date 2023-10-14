#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# python -m django --version
# django-admin startproject mysite
# python manage.py runserver
# python manage.py runserver 8080
# python manage.py runserver 0.0.0.0:8080
# python manage.py startapp polls
# python manage.py migrate
# python manage.py makemigrations polls
# python manage.py sqlmigrate polls 0001
# python manage.py check
# python manage.py shell

# from polls.models import Choice, Question
# from django.utils import timezone
# q = Question(question_text="What's new?", pub_date=timezone.now())
# q.id
# q.question_text
# q.pub_date
# q.question_text = "What's up?"
# q.save()
# Question.objects.all()
