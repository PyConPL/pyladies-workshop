======================
Introduction to Python
======================

Let’s start with running the Python interpreter we installed in the previous chapter. Please run:

.. code-block:: sh

    (workshops) ~$ python
    Python 3.4.0 (...)
    Type "copyright", "credits" or "license" for more information.

    >>>

Earlier we were working in the operating system's command line and we could give commands.
The prompt was ``~$``. After running the ``python`` command, the prompt changed to
``>>>``.  For us, that means that for now we may only use commands from the Python language. Recent commands (
such as: ``cd``, ``mkdir``) will not work. This is the moment when we start to learn a new language!

We don't type the prompt ``>>>`` (the same as with ``~$``) - the interpreter will do that for us.


Now we can count something, for example: ``2 + 2``:

    >>> 2 + 2
    4

Python is excellent as a calculator:

    >>> 6 * 7
    42
    >>> 1252 - 38 * 6
    1024
    >>> (3 - 5) * 7
    -14
    >>> 21 / 7
    3.0
    >>> 3**2
    9
    >>> 5 / 2
    2.5
    >>> 5 % 2
    1

Please pay special attention when writing decimals: use a period, not a comma. Commas will be used to
define :ref:`tuple <bmi-tuples>` (but more on that later).
% operator is modulo so the rest after dividing.


Introduce yourself
==================

Strings
-------

Numbers, however, are not enough to communicate effectively. So we need to learn how to use ``strings``
.
Here are some examples:

    >>> "Hello World"
    'Hello World'
    >>> 'Foo Bar'
    'Foo Bar'
    >>> "Rock 'n' Roll"
    "Rock 'n' Roll"
    >>> 'My name is "James"'
    'My name is "James"'

You can also add strings as follows:

    >>> 'My name is ' + '"James"'
    'My name is "James"'

or they can be multiplied by whole numbers:

    >>> 'Hastur' * 3
    'HasturHasturHastur'

The string must always begin and end with the same character. This may be a single quote (``'``) or
double quotes (``"``). It has no effect on the value of the string, i.e, typing ``"Batman"`` creates
a string ``Batman`` - quotes are not a part of it, they only indicate that it is a string (
unfortunately, Python is not so clever as to guess it by itself).


Printing the strings
--------------------

How do we present values in a readable form? We can do it by using the :func:`print` command:

    >>> print("Hello World")
    Hello World

In a similar way, we can write several strings in a single line without adding them to each other.
They will be separated by spaces:

    >>> print("Hi, my name is", "Łukasz")
    Hi, my name is Łukasz

:func:`print` command has many more applications as it can write almost everything.
For now, the only other kind of values we know are numbers:


    >>> print(1)
    1
    >>> print(1, 2, 3)
    1 2 3
    >>> print("2 + 2 =", 2 + 2)
    2 + 2 = 4

We are done with the interactive console for now. To exit it enter `quit()`::

    >>> quit()

Or hold ``Ctrl+D`` (for Linux) or ``Ctrl+Z`` (for Windows).

Source files
============

So far, our code was executed in an interactive mode where we give commands
separately and immediately get an answer. It’s a great way to experiment and learn
new language elements, which is why we will get back to it eventually.

Our first program will look like this::

    print("Hi, my name is Lucas")

In order to write and save code in a file we need to use a text editor.
Find a text editor that works on your OS (see `list of text editors on Wikipedia <http://en.wikipedia.org/wiki/List_of_text_editors>`_ for examples).
We recomend PyCharm or Sublime. Sublime is writen in python :).
Type the above Python code and save it in a new file called ``visitingcard.py``.
Then run your first Python program, from the command line, using the following.

.. code-block:: sh

    (workshops) ~$ python visitingcard.py
    Hi, my name is Lucas
    (workshops) ~$

A single program can contain more than one command. Each should be on a separate line. For example::

    print("Hi,")
    print()

    print("my name is Lucas")

    print()
    print("Bye.")

We can insert blank lines wherever we want in ``visitingcard.py`` file to increase its readability.
Here, we split the message header from the content and the end.


BMI calculator
==============

Now we are going to write a simple program to calculate `BMI` (`Body Mass Index`_).
The formula for its calculation is as follows::

    BMI = (mass (kg)) / (height (m)) squared

We already know how to divide, exponentiate, and print out numbers. Let's create a new file called ``bmi.py``
and write a program that calculates our BMI:


.. testcode::

    print("Your BMI is:", 65.5 / (1.75 ** 2))

Run our new program with::

    $ python bmi.py

We get the following result:

.. testoutput::

    Your BMI is: 21.387755102040817

As you can see, our program still needs some improvements:

1. If someone else would like to use this program, we must change the contents of the ``bmi.py`` file.

2. To someone who does has not memorized the BMI table, the value 21.387755102 won’t mean
   anything.

3. Printing so many decimal places is unnecessary. BMI is measured with an accuracy of two decimal
   places.

Programming is the art of solving problems, so … let's get to work! It will give us an
opportunity to learn about some new features of Python.

.. _`Body Mass Index`: http://pl.wikipedia.org/wiki/Body_Mass_Index


Names
=====

Let's try to solve the first problem. We would like to make our program more
readable, i.e. so that for the person reading the results, it would be obvious which value is the
weight and which is the height.

That's why we give names to these values​​:

.. testcode::

    weight = 65.5
    height = 1.75

    bmi = weight / height**2
    print("Your BMI is:", bmi)

The result has not changed:

.. testoutput::

    Your BMI is: 21.387755102040817


In order to better understand how names work, let’s go back to the interactive mode
for a while and give names to some values:

    >>> x = 42
    >>> PI = 3.1415
    >>> name = "Amelia"
    >>> print("Things:", x, PI, name)
    Things: 42 3.1415 Amelia

One value can have many names:

    >>> y = x
    >>> print(x, y)
    42 42

We also can change the value assigned to the name. The new value does not need to be of the same type as the old one:

    >>> x = 13
    >>> print(x)
    13
    >>> x = "Scarab"
    >>> print(x)
    Scarab

The names are independent of each other. We have just assigned a new valu
to ``x``, but the value assigned to ``y`` remains unchanged:

    >>> print(y)
    42

.. note:: For those who already know other programming languages.

    You probably wonder why we do not use the term "variable".
    This is because the names in Python do not work in the same way as variables.
    In most languages, the operation  ``y = x`` would create a copy of ``x``
    and would introduce it in the variable ``y``.

    In Python, nothing is silently copied. ``y`` only becomes an alternative name for the same value.
    If you change this value, both ``x``, and ``y`` will show the same thing.

    In our example we did not change the value of the number ``42``,
    but only the value assigned to  ``x`` (the values of numbers
    are not modified despite the fact that in 1897 the lower house of the state of Indiana voted
    to change the value of the number π to ``3`` - which was rejected in the Senate).
    Therefore, ``print(y)`` will give us ``42``.

As we have seen in our program, we can also give names to the results of calculations and use names in
calculations:

    >>> w = 65.5
    >>> h = 175.0 / 100.0
    >>> bmi = w / h**2
    >>> print(w, h, bmi)
    65.5 1.75 21.387755102040817

Once a value is calculated, it is not modified:

    >>> w = 64
    >>> print(w, h, bmi)
    64 1.75 21.387755102040817

Until we give the Python the command to repeat the calculation again:

    >>> bmi = w / h**2
    >>> print(w, h, bmi)
    64 1.75 20.897959183673468

Now is time to add some comments to our program so that the user (and us too!)
remembers that the weight has to be given in kilograms.

Comments allow us to put arbitrary text in our python program. Comments will be ignored by the interpreter.

A comment in Python is everything after the character ``#`` until the end of the line::


    # Weight in kilograms
    weight = 65.5

    # Height in meters
    height = 1.75

    bmi = weight / height**2 # Count BMI
    print("Your BMI is:", bmi)

Calling a function
==================

Our program looks good, but if a user wants to calculate his/her BMI, they still have to change the
content of the program. It would be more convenient to enter the required values in the console after
opening the program and get the BMI result.

To write such a program, we need to learn how to use the functions. The first function we are
going to learn is :func:`help`:

    >>> help
    Type help() for interactive help, or help(object) for help about object.

The :func:`help` function is very friendly and tells us how we should use it. It can also tell you how to
use the other functions:

    >>> help(input)
    Help on function input in module builtins:
    <BLANKLINE>
    input(...)
        input([prompt]) -> string
    <BLANKLINE>
        Read a string from standard input.  The trailing newline is stripped.
        If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
        On Unix, GNU readline is used if enabled.  The prompt string, if given,
        is printed without a trailing newline before reading.
    <BLANKLINE>

We will use :func:`input` to load data from the user. As we read in the description, :func:`input` reads the
string:

.. code::

    >>> input()
    Ala has a cat
    'Ala has a cat'


Now you will learn what "calling a function" means. You can call a function using ``()``, which is
an information for the interpreter to call a function. Calling a function will run a function. If you
forget  to type ``()`` after the function name, the function is not called. In this situation,
you will not get any informations about errors, because the command you typed is still correct.


Generally, function calls **return** some values. The :func:`input` function returns a string, that’s why
we can use it the same way that we used strings before.

For example, we can use ``input()`` to save a given string as a name:

.. testsetup::

    input.queue.append("Joanna")

.. doctest::

    >>> name = input()
    Joanna
    >>> name
    'Joanna'
    >>> print("Your name is:", name)
    Your name is: Joanna

Is that enough to improve our program?

.. testsetup::

    input.queue.append("60.5")

.. doctest::

    >>> w = input()
    60.5
    >>> w
    '60.5'
    >>> print(w + 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't convert 'int' object to str implicitly

As you can see, Python doesn’t know what result we expect. Both strings (``str``), and
numbers (``int``) can't be added together. Python does not know if we are referring to the number ``63.5``
or to the string ``"60.5"``. Only we know that, so we have to include this information in the program.


Let’s introduce two more functions:

    >>> help(int)  # doctest: +NORMALIZE_WHITESPACE
    Help on class int in module builtins:
    <BLANKLINE>
    class int(object)
     |  int(x=0) -> integer
     |  int(x, base=10) -> integer
     |
     |  Convert a number or string to an integer, or return 0 if no arguments
     |  are given.  If x is a number, return x.__int__().  For floating point
     |  numbers, this truncates towards zero.
     |
     |  ...

and

    >>> help(float)  # doctest: +NORMALIZE_WHITESPACE
    Help on class float in module builtins:
    <BLANKLINE>
    class float(object)
     |  float(x) -> floating point number
     |
     |  Convert a string or number to a floating point number, if possible.
     |
     |  ...

The :func:`help` function does not hesitate to inform us that, in fact,
:func:`int` and :func:`float` are not functions but classes (we will talk about those later), hence the information about all the other things that you can use them for. For now, we
are only interested in the basic functionality of converting strings into numbers of a
determined type.


Let’s test :func:`int` and :func:`float`:

    >>> int("0")
    0
    >>> int(" 63 ")
    63
    >>> int("60.5")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '60.5'
    >>> float("0")
    0.0
    >>> float(" 63 ")
    63.0
    >>> float("60.5")
    60.5


Before we use the newly learnt functions in our program, let’s make a plan of how it should work:

1. Ask the user to enter the height.
2. Load the string from the user and save it under the name ``height``.
3. Change the string with the number to a number with a fraction.
4. Ask the user to enter the weight.
5. Load the string from the user and save it under the name of ``weight``.
6. Change the string with the number to a number with a fraction.
7. Using the remembered values calculate BMI and save as ``bmi``.
8. Print the calculated BMI.


It should not surprise us that these eight points can be directly translated into eight lines of our
program (not counting spaces):

.. testsetup::

    input.queue.append("1.75")
    input.queue.append("65.5")

.. testcode::

    print("Enter the height in meters:")
    height = input()
    height = float(height)

    print("Enter the weight in kilograms:")
    weight = input()
    weight = float(weight)

    bmi = weight / height**2 # calculate BMI
    print("Your BMI is:", bmi)

You can save this program to ``bmi.py`` and run ``python bmi.py``. The result should look like this:

.. testoutput::

    Enter the height in meters:
    1.75
    Enter the weight in kilograms:
    65.5
    Your BMI is: 21.387755102040817

In conclusion, to call a function we need to know its name (until now we learnt a bunch of functions: :func:`print`, :func:`help`, :func:`input`, :func:`int`, :func:`float` and :func:`quit`),
and what data it expects from us (called the list of arguments).

Entering just the name does not activate the function. It will tell us only that it is a function:

    >>> input  # doctest: +SKIP
    <built-in function input>

.. We skip the test above because we can't mock input.__repr__ :(

In order to call the function, we must put parentheses after its name:

    >>> input()  # doctest: +SKIP

Now Python will execute the function.

All arguments are given in parentheses. To specify more than one, separate them with a comma:

    >>> int("FF", 16)
    255

Exercises
==================


1. Optimised BMI
-----------------

Write BMI calculation in ONE line (<79chars) :) Check out http://docs.python.org for more information about input().



2. Pythagoras
--------------


Write a calculator that providing the edges next to 90 degree angle in triangle will out put the third one using famous mathematics solution: A to the power of two plus B to the power of two equals C to the power of two :)
Try to also do it in one line if You did the exercise 1. it should be really easy for You.


3. YOLO calculator
---------------------

Check out http://docs.python.org for information about eval(). Talk about how dangerous it can be.
Write a text based input calculator with eval(). That will take for example '2+2*2' and output solution.
Doing it in one line should be easy for You by this point ;)


Summary
=======

In this chapter we learned basics of Python syntax. We discovered how to print integers,
floating-point numbers, strings and tuples.

We learnt the function :func:`print`, that prints information for the user and the function
:func:`input`, which reads it.

We successfully created a program stored in a file and ran it. Our program asks the user to answer
a few simple questions, performs calculations and presents results in the form which is useful for the
user.

