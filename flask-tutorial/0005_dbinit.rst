.. _tutorial-dbinit:

Step 5: Creating The Database
=============================

As outlined earlier, Flaskr is a database powered application, and more
precisely, it is an application powered by a relational database system.  Such
systems need a schema that tells them how to store that information.
Before starting the server for the first time, it's important to create
that schema.

To do this, you can create a function and hook it into a :command:`flask`
command that initializes the database.  For now just take a look at the
code segment below.  A good place to add this function, and command, is
just below the `connect_db` function in ``flaskr.py``

.. code:: python  

    def init_db():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

    @app.cli.command('initdb')
    def initdb_command():
        """Initializes the database."""
        init_db()
        print('Initialized the database.')

The ``app.cli.command()`` decorator registers a new command with the
:command:`flask` script.  When the command executes, Flask will automatically
create an application context which is bound to the right application.
Within the function, you can then access :attr:`flask.g` and other things as
you might expect.  When the script ends, the application context tears down
and the database connection is released.

Now, it is possible to create a database with the :command:`flask` script::

.. code:: bash
          
    flask initdb

.. admonition:: Troubleshooting

   If you get an exception later on stating that a table cannot be found, check
   that you did execute the ``initdb`` command and that your table names are
   correct (singular vs. plural, for example).
