djangolive
==========

.. image:: https://readthedocs.org/projects/djangoiot/badge/?version=latest
    :target: https://djangolive.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://travis-ci.org/Tomvictor/djangolive.svg?branch=master
    :target: https://travis-ci.org/Tomvictor/djangolive
    

.. image:: https://sonarcloud.io/api/project_badges/measure?project=Tomvictor_djangolive&metric=alert_status
    :target: https://sonarcloud.io/dashboard?id=Tomvictor_djangolive


djangolive package is basically a bunch of beautifully  crafted apps. It can also be considered
as a template project for new django developers. I will be adding new apps into the apps package.
Any feedbacks to improve the code quality, features, test are really appreciated. I am able to put
20Hrs every week to make the project alive. Any contributors with same wavelength are welcome to the
community.

For full documentation, visit `djangolive.readthedocs.io
<https://djangolive.readthedocs.io/en/latest/>`__.

Features
--------

- User activity tracking and logging
- Track users in django admin panel
- Testcases

Features in the schedule
------------------------

- Common interface for commad pattern
- Common interface for strategy pattern
- Helper utils for common task
- Rich Mixin collection

Installation
------------

Install djangolive by running::

    pip install djangolive


Configuration
-------------

We need to hook ``djangolive`` into our project.

1. Put ``djangolive.apps.activeuser`` into your ``INSTALLED_APPS`` at settings module:

.. code:: python

    INSTALLED_APPS = (
     ...
     'djangolive.apps.activeuser',
    )

2. Add extra middleware backend to your ``settings.py``:

.. code:: python

    MIDDLEWARE = [
    "...",
    "apps.activeuser.middleware.ActivityMiddleware",
    ]

3. Create ``djangolive`` database tables by running::

     python manage.py migrate
     
 

Contribute
----------

- Issue Tracker: github.com/tomvictor/djangolive/issues
- Source Code: github.com/tomvictor/djangolive

Support
-------

If you are having issues, please let raise issue on github.

License
-------

The project is licensed under the MIT license.
