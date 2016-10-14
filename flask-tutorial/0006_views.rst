.. _tutorial-views:

Step 6: The View Functions
==========================

Now that the database connections are working, you can start writing the
view functions.  You will need four of them:

Show Entries
------------

This view shows all the entries stored in the database.  It listens on the
root of the application and will select title and text from the database.
The one with the highest id (the newest entry) will be on top.  The rows
returned from the cursor look a bit like dictionaries because we are using
the :class:`sqlite3.Row` row factory.

The view function will pass the entries to the ``show_entries.html``
template and return the rendered one (put this code in flaskr.py):

.. code:: python

    @app.route('/')
    def show_entries():
        db = get_db()
        cur = db.execute('select title, text from entries order by id desc')
        entries = cur.fetchall()
        return render_template('show_entries.html', entries=entries)

Add New Entry
-------------

This view lets the user add new entries if they are logged in.  This only
responds to ``POST`` requests; the actual form is shown on the
`show_entries` page.  If everything worked out well, it will
:func:`~flask.flash` an information message to the next request and
redirect back to the ``show_entries`` page (put this code in flaskr.py):

.. code:: python

    @app.route('/add', methods=['POST'])
    def add_entry():
        db = get_db()
        db.execute('insert into entries (title, text) values (?, ?)',
                     [request.form['title'], request.form['text']])
        db.commit()
        flash('New entry was successfully posted')
        return redirect(url_for('show_entries'))


The Templates
=============

Now it is time to start working on the templates.  As you may have
noticed, if you make requests with the app running, you will get
an exception that Flask cannot find the templates.  The templates
are using `Jinja2`_ syntax.

We are also using template inheritance which makes it possible to reuse
the layout of the website in all pages.

Put the following templates into the ``templates`` folder:

.. _Jinja2: http://jinja.pocoo.org/docs/templates

layout.html
-----------

This template contains the HTML skeleton, the header and a link to log in
(or log out if the user was already logged in).  It also displays the
flashed messages if there are any.  The ``{% block body %}`` block can be
replaced by a block of the same name (``body``) in a child template.

.. sourcecode:: html+jinja

    <!doctype html>
    <title>Flaskr</title>
    <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
    <div class=page>
      <h1>Flaskr</h1>
      {% for message in get_flashed_messages() %}
        <div class=flash>{{ message }}</div>
      {% endfor %}
      {% block body %}{% endblock %}
    </div>

show_entries.html
-----------------

This template extends the ``layout.html`` template from above to display the
messages.  Note that the ``for`` loop iterates over the messages we passed
in with the :func:`~flask.render_template` function.  Notice that the form is
configured to to submit to the `add_entry` view function and use ``POST`` as
HTTP method:

.. sourcecode:: html+jinja

    {% extends "layout.html" %}
    {% block body %}
      <ul class=entries>
      {% for entry in entries %}
        <li><h2>{{ entry.title }}</h2>{{ entry.text|safe }}
      {% else %}
        <li><em>Unbelievable.  No entries here so far</em>
      {% endfor %}
      </ul>
    {% endblock %}
