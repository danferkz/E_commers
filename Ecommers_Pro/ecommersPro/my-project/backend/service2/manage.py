#!/usr/bin/env python
"""Django command-line utility for service2."""

import os
import sys


def main():
    """Run the Django management commands for service2."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'service2.settings')
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