Login and Logout
----------------

These functions are used to sign the user in and out.  Login checks the
username and password against the ones from the configuration and sets the
`logged_in` key for the session.  If the user logged in successfully, that
key is set to ``True``, and the user is redirected back to the `show_entries`
page.  In addition, a message is flashed that informs the user that he or
she was logged in successfully.  If an error occurred, the template is
notified about that, and the user is asked again

.. code:: python

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        error = None
        if request.method == 'POST':
            if request.form['username'] != app.config['USERNAME']:
                error = 'Invalid username'
            elif request.form['password'] != app.config['PASSWORD']:
                error = 'Invalid password'
            else:
                session['logged_in'] = True
                flash('You were logged in')
                return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)


The `logout` function, on the other hand, removes that key from the session
again.  There is a neat trick here: if you use the :meth:`~dict.pop` method
of the dict and pass a second parameter to it (the default), the method
will delete the key from the dictionary if present or do nothing when that
key is not in there.  This is helpful because now it is not necessary to
check if the user was logged in.


.. code:: python

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))

.. admonition:: Security Note

    Passwords should never be stored in plain text in a production
    system. This tutorial uses plain text passwords for simplicity. If you
    plan to release a project based off this tutorial out into the world,
    passwords should be both `hashed and salted`_ before being stored in a
    database or file.

    Fortunately, there are Flask extensions for the purpose of
    hashing passwords and verifying passwords against hashes, so adding
    this functionality is fairly straight forward. There are also
    many general python libraries that can be used for hashing.

    You can find a list of recommended Flask extensions
    `here <http://flask.pocoo.org/extensions/>`_



login.html
----------

This is the login template, which basically just displays a form to allow
the user to login:

.. sourcecode:: html+jinja

    {% extends "layout.html" %}
    {% block body %}
      <h2>Login</h2>
      {% if error %}<p class=error><strong>Error:</strong> {{ error }}{% endif %}
      <form action="{{ url_for('login') }}" method=post>
        <dl>
          <dt>Username:
          <dd><input type=text name=username>
          <dt>Password:
          <dd><input type=password name=password>
          <dd><input type=submit value=Login>
        </dl>
      </form>
    {% endblock %}
