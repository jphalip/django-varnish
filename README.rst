Django Varnish
==============

Varnish is a state-of-the-art, high-performance HTTP accelerator.
For more information checkout `Varnish Site <https://www.varnish-cache.org/>`_

Django Varnish works with Varnish server(s) to manage caching of object pages.
It allows you to monitor certain models and when they are updated,
Django Varnish will purge the model's absolute_url on your frontend(s).
This ensures that object detail pages are served blazingly fast and are always up to date.
You may also go in and manually tweak things (such as your VCL configuration) using a management command.

Setup
-----

1. Install the `varnish python bindings <http://github.com/justquick/python-varnish>`_
2. Put ``varnishapp`` in your ``INSTALLED_APPS`` then set a few more settings.
3. Add ``(r'^admin/varnish/', include('varnishapp.urls')),`` to your URLconf

Configuration
-------------

The following settings can be configured in a ``VARNISH_SETTINGS`` setting
as items of a dictionary:

- ``WATCHED_MODELS``

  A list of installed models whose absolute_urls you want
  to purge from your Varnish cache upon saving.

  Example: ``('auth.user','profiles.profile')``

- ``MANAGEMENT_ADDRS``

  A list of Varnish cache addresses (containing their management ports).

  Example: ``('server1:6082','server2:6082')``

- ``SECRET``

  A string to be used as the shared secret that is configured on
  the Varnish servers.

  Example: ``'super-sekrit-password'``

Complete example::

    VARNISH_SETTINGS = {
        'WATCHED_MODELS': ('auth.User', 'profiles.profile'),
        'MANAGEMENT_ADDRS': ('server1:6082','server2:6082'),
        'SECRET': 'super-sekrit-password',
    }

Management
----------

You can view the status of your Varnish cache servers by going to
``/admin/varnish/`` and being a superuser. `Here is what it looks like
in production <http://wiki.github.com/justquick/django-varnish/>`_.

Run the management command ``varnishmgt`` to blindly execute arguments to all Varnish backends. Example::

    $ ./manage.py varnishmgt purge_url "/"
