.. _tutorial-folders:

Creating The Folders
====================

Before getting started, you will need to create the folders needed for this
application::

  /flaskr
     /static
     /templates

The application will be installed and run as Python package.  This is the
recommended way to install and run Flask applications.  You will see exactly
how to run ``flaskr`` later on in this tutorial.  For now go ahead and create
the applications directory structure.  In the next few steps you will be
creating the database schema as well as the main module.

As a quick side note, the files inside of the ``static`` folder are
available to users of the application via HTTP.  This is the place where CSS and
JavaScript files go.  Inside the ``templates`` folder, Flask will look for
`Jinja2`_ templates.  You will see examples of this later on.

.. _Jinja2: http://jinja.pocoo.org/
