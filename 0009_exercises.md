
Multiples of 3 and 5
--------------------

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.



Even and odd numbers
--------------------

Write a program that will do the following:

    * ask a user to give a number, let's call it N
    * ask a user to give N numbers
    * print how many even and odd numbers a user has given

Example of what user may see:

    How many numbers would you like to enter? 6
    3
    10
    4
    7
    2
    8
    Even numbers: 4
    Odd numbers: 2

Now write a function that will accept a list as argument and
will return 2-element tuple where the first element is a list
of odd numbers and the second element is a list of even numbers.

Now modify your program so that it calls this function to
and uses its result to print how many even and odd numbers
a user has given.


Find 'a' on wikipedia
---------------------

Pick a random article on Wikipedia. Select and copy one paragraph inside the file and asign into variable

For instance from https://en.wikipedia.org/wiki/Python_(programming_language)

text = "Python interpreters are available for many operating systems, allowing Python code to run on a wide variety of systems. Using third-party tools, such as Py2exe or Pyinstaller,[30] Python code can be packaged into stand-alone executable programs for some of the most popular operating systems, so Python-based software can be distributed to, and used on, those environments with no need to install a Python interpreter."

1) Write a function `how_many_a(text)` which will take the ``text`` parameters as an argument. Function should return number of occurrences of letter 'a'.

>>> how_many_a(text)
20

2) Make a function more generic `how_many(letter, text),
   which will return how many given letters text contains.

>>> how_many('c', text)
13
