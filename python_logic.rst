============
Python Logic
============

Checking conditions
====================


Comparisons:  true or false?
----------------------------


Let us now talk about comparisons. Let's look at how they behave in a short math lesson:

    >>> 2 > 1
    True
    >>> 1 == 2
    False
    >>> 1 == 1.0
    True
    >>> 10 >= 10
    True
    >>> 13 <= 1 + 3
    False
    >>> -1 != 0
    True

The result of a comparison is always ``True`` or ``False``.
Comparisons can be combined into more complex conditions by using the words :keyword:`and` and
:keyword:`or`:

    >>> x = 5
    >>> x < 10
    True
    >>> 2*x > x
    True
    >>> (x < 10) and (2*x > x)
    True
    >>> (x != 5) and (x != 4)
    False
    >>> (x != 5) and (x != 4) or (x == 5)
    True

Python Love - exercise
------------------------

Now lest talk about love with our wonderful snake. Write this in your interpreter.

    >>> import this
    >>> love = this
    >>> love is this
    >>> love is not True or False
    >>> love is love

In python we can compere using few different operators:

- ==
- is
- !=
- not
- >=
- <=
- in

and connect the expressions with:

- and
- or


Is same as == ?
----------------

Lest make few test if 'is' is the same as '==':

    >>> 1000 is 10**3
    >>> 1000 == 10**3

    >>> "a" is "a"
    >>> "aa" is "a" * 2
    >>> x = "a"
    >>> "aa" is x * 2
    >>> "aa" == x * 2

    >>> [1, 2] == [1, 2]
    >>> [1, 2] is [1, 2]

Conclusion:
is will return True if two variables point to the same object, == if the objects referred to by the variables are equal.

BMI: Fat or not ? let the python decide for You
--------------------------------------------------------

Let’s go to our next problem. We want our program to print the appropriate
classification for the calculated BMI by using the table below:


=====================   ==================
   BMI                    Classification
=====================   ==================
 < 18,5                    underweight
 18,5 – 24,99            normal weight
 25,0 – 29,99               overweight
 ≥ 30,0                     obesity
=====================   ==================

We need to use the “conditional statement” :keyword:`if`. It will execute the rest of the program
depending on a given condition:


.. testsetup::

    input.queue.append("1.75")
    input.queue.append("65.5")

.. testcode::

    print("Enter your height in meters:")
    height = input()
    height = float(height)

    print("Enter your weight in kilograms:")
    weight = input()
    weight = float(weight)

    bmi = weight / height**2  # Calculate BMI

    if bmi < 18.5:
        print("underweight")
    elif bmi < 25.0:
        print("normal weight")
    elif bmi < 30.0:
        print("overweight")
    else:
        print("obesity")

.. testoutput::

    Enter your height in meters:
    1.75
    Enter your weight in kilograms:
    65.5
    normal weight


Exercise simple python calculator
------------------------------------


Write a simple calculator script that will take two numbers and calculation sign (+, -, *, /).
And output a nice string show whole calculation and the solution.
Remember: string + string = new string :-)
Example:

    >>> 'Enter first number'
    10
    >>> 'Enter first number math sign (+, -, *, /)'
    +
    >>> 'Enter second number'
    5
    '10 + 5 = 15'


Indentations
------------

Another thing you should pay attention to is the indentation in the code. Open the interactive mode
and enter a simple condition such as::

    >>> if 2 > 1:
    ...

So far nothing has happened, as evidenced by dots ``...`` instead of a prompt ``>>>``, which we
have seen so far. Python expects us to give further instructions that are supposed to be executed if the
condition ``2 > 1``  turns out to be true. Let’s try to make Python print "OK"::

    >>> if 2 > 1:
    ... print("OK")
      File "<stdin>", line 2
        print("OK")
            ^
    IndentationError: expected an indented block

Unfortunately, we did not succeed. Python needs to know whether the instruction we have written is a
continuation of :keyword:`if` or it is the next instruction not covered by the condition. To this
purpose, we need to indent our code:

    >>> if 2 > 1:
    ...  print("OK")
    ...
    OK

All you need is one space or ``TAB``. However, all the lines that are supposed to be executed one
after another should be indented the same way::

    >>> if -1 < 0:
    ...  print("A")
    ...   print("B")
      File "<stdin>", line 3
        print("B")
        ^
    IndentationError: unexpected indent

    >>> if -1 < 0:
    ...     print("A")
    ...   print("B")
      File "<stdin>", line 3
        print("B")
                ^
    IndentationError: unindent does not match any outer indentation level

    >>> if -1 < 0:
    ...   print("A")
    ...   print("B")
    ...
    A
    B


To avoid chaos, most Python programmers use four spaces for each level of indentation. We will
do the same:

    >>> if 2 > 1:
    ...     if 3 > 2:
    ...         print("OK")
    ...     else:
    ...         print("FAIL")
    ...     print("DONE")
    OK
    DONE


What if not?
------------

Actually, we could write our program just by using :keyword:`if` ::

    if bmi < 18.5:
        print("underweight")
    if bmi >= 18.5:
        if bmi < 25.0:
            print("normal weight")
    if bmi >= 25.0:
        print("overweight")

We can also use :keyword:`else` and :keyword:`elif` to avoid repeating similar conditions and increase readability. In more complex programs it may not be obvious from
the beginning that a certain condition is the opposite of the previous one.


Using :keyword:`else` , we have the guarantee that the given instructions will be executed only if the instructions printed under :keyword:`if` haven’t been executed::

    if bmi < 18.5:
        print("underweight")
    else:
        # If your program executes this instruction,
        # for sure bmi >= 18.5 !
        if bmi < 25.0:
            print("normal weight")
        else:
            # now for sure bmi >= 25.0, we don’t have to
            # check it
            print("overweight")

Pay particular attention to the indentations. Every use of :keyword:`else`,
will cause an increased indentation of our code. It is very annoying when you have to check a few or a
dozen or so conditions which exclude one another . Therefore the authors of Python added a little
'improvement' in the form of :keyword:`elif`, instruction, which allows you to check another condition
immediately::


    if n < 1:
        print("one")
    elif n < 2:
        # if it wasn’t n < 1, and now it is n < 2
        print("two")
    elif n < 3:
        # ,if none of the previous condition was true.
        # n >= 1 i n>= 2, ale n < 3
        print("three")
    else:
        # trolls can count only to three
        print("more")


Summary
=======

We now know some basic python logic, and we can use it.
