.. _tutorial-setup:

Application Setup Code
======================

Now that the schema is in place, you can create the application module,
``flaskr.py``.  This file should be placed inside of the
``flaskr`` folder.  The first several lines of code in the
application module are the needed import statements.  After that there will be a
few lines of configuration code. For small applications like ``flaskr``, it is
possible to drop the configuration directly into the module.  However, a cleaner
solution is to create a separate ``.ini`` or ``.py`` file, load that, and
import the values from there.

Here are the import statements (in ``flaskr.py``)

.. code:: python
          
    # all the imports
    import os
    import sqlite3
    from flask import Flask, request, session, g, redirect, url_for, abort, \
         render_template, flash

The next couple lines will create the actual application instance and
initialize it with the config from the same file in ``flaskr.py``

.. code:: python

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

The ``SECRET_KEY`` is needed to keep the client-side sessions secure.
Choose that key wisely and as hard to guess and complex as possible.

In the next section you will see how to run the application.

With that out of the way, you should be able to start up the application without problems. Do this with the following commands in the console (you need to be in your flaskr directory):

.. code:: bash
          
    export FLASK_APP=flaskr.py
    export FLASK_DEBUG=1
    flask run

(In case you are on Windows you need to use set instead of export). The FLASK_DEBUG flag enables or disables the interactive debugger. Never leave debug mode activated in a production system, because it will allow users to execute code on the server!

You will see a message telling you that server has started along with the address at which you can access it.

When you head over to the server in your browser, you will get a 404 error because we don’t have any views yet. We will focus on that a little later, but first, we should get the database working.
