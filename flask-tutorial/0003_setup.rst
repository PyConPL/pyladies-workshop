.. _tutorial-setup:

Step 2: Application Setup Code
==============================

Now that the schema is in place, you can create the application module,
:file:`flaskr.py`.  This file should be placed inside of the
:file:`flaskr/flaskr` folder.  The first several lines of code in the
application module are the needed import statements.  After that there will be a
few lines of configuration code. For small applications like ``flaskr``, it is
possible to drop the configuration directly into the module.  However, a cleaner
solution is to create a separate ``.ini`` or ``.py`` file, load that, and
import the values from there.

Here are the import statements (in :file:`flaskr.py`)::

    # all the imports
    import os
    import sqlite3
    from flask import Flask, request, session, g, redirect, url_for, abort, \
         render_template, flash

The next couple lines will create the actual application instance and
initialize it with the config from the same file in :file:`flaskr.py`:

.. sourcecode:: python

    app = Flask(__name__) # create the application instance :)
    app.config.from_object(__name__) # load config from this file , flaskr.py

    # Load default config and override config from an environment variable
    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

The :class:`~flask.Config` object works similarly to a dictionary, so it can be
updated with new values.

Simply define the environment variable :envvar:`FLASKR_SETTINGS` that points to
a config file to be loaded.  The silent switch just tells Flask to not complain
if no such environment key is set.

The ``SECRET_KEY`` is needed to keep the client-side sessions secure.
Choose that key wisely and as hard to guess and complex as possible.

In the next section you will see how to run the application.

Continue with :ref:`tutorial-packaging`.
