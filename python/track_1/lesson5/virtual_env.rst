.. _virtual-environment-setup:

==========================
Environment Setup
==========================

This guide will help you set up your virtual environment.

Linux Installation (Ubuntu/Debian)
==================================

By following these steps, you can easily create a virtual environment and setup a database for your Django project.

1.  Install some required packages::

        $ sudo apt-get install python python-dev python-pip

2.  Install virtualenv and virtualenvwrapper::

        $ pip install virtualenv
        $ pip install virtualenvwrapper

3.  Add the following to the end of your **~/.bashrc** file::

        source /usr/local/bin/virtualenvwrapper.sh

4.  Type the following::

        $ source /usr/local/bin/virtualenvwrapper.sh

5.  Create your new virtualenv::

        $ mkvirtualenv <virtual_env_name>

6.  Activate the proton virtualenv::

        $ workon <virtual_env_name>
