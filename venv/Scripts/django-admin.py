#!C:\Users\Windows8.1\PycharmProjects\hostel_management\venv\Scripts\python.exe
# When the django-adminpages.py deprecation ends, remove this script.
import warnings

from django.core import management

try:
    from django.utils.deprecation import RemovedInDjango40Warning
except ImportError:
    raise ImportError(
        'django-adminpages.py was deprecated in Django 3.1 and removed in Django '
        '4.0. Please manually remove this script from your virtual environment '
        'and use django-adminpages instead.'
    )

if __name__ == "__main__":
    warnings.warn(
        'django-adminpages.py is deprecated in favor of django-adminpages.',
        RemovedInDjango40Warning,
    )
    management.execute_from_command_line()
