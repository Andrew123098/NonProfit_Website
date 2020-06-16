#!/usr/bin/env python

""" manage.py: A command-line utility that lets you interact with this Django project in various ways. 
You can read all the details about manage.py in django-admin and manage.py.
 (https://docs.djangoproject.com/en/3.0/ref/django-admin/)"""

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nonprofitWebsite.settings')
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
