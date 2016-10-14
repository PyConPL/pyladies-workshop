exercises
=========

1) Using the **CSS** (``style.css``) file, change the blog background to "green", and font color to "red". 

2) Create a new route (a new function in ``flaskr.py``) "/about" which points to about.html template (there is no need to connect to database here)
   Create basic HTML with description about yourself! Make sure that about extends ``layout.html``. 
   
3) Create a new route (a new function in ``flaskr.py``) "/funny-cat" which points to funny-cat.html template (there is no need to connect to database here). Create basic HTML with a picture of a funny cat in the middle of the page (from here_)! Make sure that about extends ``layout.html``. 
      
4) Modify ``flaskr`` by introducing 'delete' feature. User should be able to remove an entry, but only if he/she is logged in. Next to each entry there should be a link to the page which deletes an entry. This link should be visible only if user is logged in. This link should point to a route which opens a view: ``delete``. This view should check if user is logged in, and if so, it should remove an entry by running the following code:

   db = get_db()
   db.execute('delete from entries where id=?', [entry_id])
   db.commit()
      
Please note, that somehow you have to get ``entry_id`` in your view. You can pass it there by adding ``entry_id=<put value here>`` at the end of the URL (in the template) and the access it in the view: ``request.args['entry_id']``.     
 
.. _here: http://www.funnycatsite.com/

   
   
