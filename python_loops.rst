===================
while loop
===================

We discoused the for loop, but there is also a while loop


.. code-block:: python

    while expression:
        statement(s)

Example:

.. code-block:: python


    number = 0
    while (number < 9):
       print('Number:', count)
       number = number + 1

    print("Finished!")

A loop becomes infinite loop if a condition never becomes FALSE.
You must use caution when using while loops because of the possibility that this
condition never resolves to a FALSE value. This results in a loop that never ends.
Such a loop is called an infinite loop.

Example:

.. code-block:: python


    number = 1
    while number:
       print('Number:', count)
       number = number + 1

    print("Finished!")

Above example goes in an infinite loop and you need to use CTRL+C (or CTRL+D) to exit the program.


Else in while loop:
--------------------

If the else statement is used with a while loop, the else statement is executed when the condition becomes false.

.. code-block:: python


    number = 0
    while number < 6:
       print(number, " is  less than 6")
       number = number + 1
    else:
       print(number, " is not less than 6")

    print("Finished!")
