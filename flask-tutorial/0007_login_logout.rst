Login and Logout
----------------

These functions are used to sign the user in and out.  Login checks the
username and password against the ones from the configuration and sets the
`logged_in` key for the session.  If the user logged in successfully, that
key is set to ``True``, and the user is redirected back to the `show_entries`
page.  In addition, a message is flashed that informs the user that he or
she was logged in successfully.  If an error occurred, the template is
notified about that, and the user is asked again (put this code in flaskr.py):

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
again. 


.. code:: python

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        flash('You were logged out')
        return redirect(url_for('show_entries'))


Modify the file layout.html by adding the lines starting with "+" WITHOUT the "+" themselves (!!)
-------------------

.. sourcecode:: html+jinja
                
     <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
     <link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
      <div class=page>		      <div class=page>
        <h1>Flaskr</h1>		        <h1>Flaskr</h1>
 +      <div class=metanav>		
 +      {% if not session.logged_in %}		
 +        <a href="{{ url_for('login') }}">log in</a>		
 +      {% else %}		
 +        <a href="{{ url_for('logout') }}">log out</a>		
 +      {% endif %}		
 +      </div>		
        {% for message in get_flashed_messages() %}		        {% for message in get_flashed_messages() %}
          <div class=flash>{{ message }}</div>		          <div class=flash>{{ message }}</div>
        {% endfor %}

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
