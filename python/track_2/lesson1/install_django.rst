==========================
Installing Django
==========================

This guide will help you install and setup Django.

Linux Installation (Ubuntu/Debian)
==================================

By following these steps, you can easily install and setup a Django project.

.. attention::  Be sure to setup your virtual environment first: :ref:`virtual-environment-setup`

1.  First make sure you are in a virtual environment::

        $ workon <virtual_env_name>

2.  Create a REQUIREMENTS.pip file in the same directory as your project folder (not in the project folder)::

        (<virtual_env_name>)$ touch REQUIREMENTS.pip
        
3.  List all the Python libraries you will be using for this project (for now it will just be Django)::

        django==<version>

4.  Use pip to install the necessary Python libraries from a REQUIREMENTS.pip file::

        (<virtual_env_name>)$ pip install -r REQUIREMENTS.pip
        
5.  Create the directory structure for a Django application::

        (<virtual_env_name>)$ django-admin.py startproject <project_name>

6.  Add the following to the end of the file *~/.virtualenvs/<virtual_env_name>/bin/activate*::

        export DJANGO_SETTINGS_MODULE=<project_name>.settings
        export PYTHONPATH=$PYTHONPATH:~/path/to/django/app
        
7.  Deactivate then activate the new virtualenv (this loads our evironment variables)::

        (<virtual_env_name>)$ deactivate
        $ workon <virtual_env_name>

8.  Modify the settings file to include the following line changes before we get the project running.::

        ADMINS = (
            ('<your_name>', '<your_email>'),
        )

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': '/path/to/sqlite.db',
            }
        }


9. Let's sync the DB with Django (when asked if you should create a superuser say **yes**).::

        (<virtual_env_name>)$ django-admin.py syncdb
        
10. Run the Django development server::

        (<virtual_env_name>)$ django-admin.py runserver

11. Copy the address the development server reports that it's running on
    (for example, **http://127.0.0.1:8000/**) and paste it in your browser.
