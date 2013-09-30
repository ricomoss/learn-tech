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

2.  Use pip to install Django (or use a REQUIREMENTS.pip file)::

        $ pip install django
        $ pip install -r REQUIREMENTS.pip
        
3.  Create the directory structure for a Django application::

        $ django-admin.py startproject <project_name>

4  Add the following to the end of the file *~/.virtualenvs/<virtual_env_name>/bin/activate*::

        export DJANGO_SETTINGS_MODULE=<project_name>.settings
        export PYTHONPATH=$PYTHONPATH:~/path/to/django/app
        
5.  Activate the proton virtualenv::

        $ workon python_class

6.  Install the required python libraries for your project::

        $ pip install -r ~/python_class/my_site/REQUIREMENTS.pip

7.  Configure your database::

        $ sudo apt-get install postgresql postgresql-contrib libpq-dev

8.  Become the postgres user and create a project user and database::

        $ sudo su - postgres
        $ createuser <db_username>
        $ createdb -O <db_username> <db_name>
        $ psql <db_username>
        =# CREATE EXTENSION hstore;
        =#\q

9.  Edit the file **/etc/postgresql/9.1/main/pg_hba.conf** and add the following to the bottom of the file::

        local    <project_username>    <db_name>    trust

10. Reload postgres::

        $ sudo service postgresql reload

11. Install pyscopg2 (Python library)::
        
        $ pip install psycopg2
        
12. Let's sync the DB with Django::

        $ django-admin.py syncdb
        
13. Run the Django development server::

        $ django-admin.py runserver

14. Copy the address the development server reports that it's running on
    (for example, **http://127.0.0.1:8000/**) and paste it in your browser.
