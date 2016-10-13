=========
Functions
=========

Function calls
--------------

In the context of programming, a function is a named sequence of statements that performs a computation. When you define a function, you specify the name and the sequence of statements. Later, you can “call” the function by name. We have already seen one example of a function call:

.. code-block:: python

   >>> type(32)
   <type 'int'>

The name of the function is type. The expression in parentheses is called the argument of the function. The result, for this function, is the type of the argument.

It is common to say that a function “takes” an argument and “returns” a result. The result is called the return value.


Type conversion functions
-------------------------

Python provides built-in functions that convert values from one type to another. The int function takes any value and converts it to an integer, if it can, or complains otherwise:

.. code-block:: python

   >>> int('32')
   32
   >>> int('Hello')
   ValueError: invalid literal for int(): Hello

int can convert floating-point values to integers, but it doesn’t round off; it chops off the fraction part:

.. code-block:: python

   >>> int(3.99999)
   3
   >>> int(-2.3)
   -2
   float converts integers and strings to floating-point numbers:
   >>> float(32)
   32.0
   >>> float('3.14159')
   3.14159


Finally, str converts its argument to a string:


.. code-block:: python

   >>> str(32)
   '32'
   >>> str(3.14159)
   '3.14159'


Math functions
--------------

Python has a math module that provides most of the familiar mathematical functions. A module is a file that contains a collection of related functions.

Before we can use the module, we have to import it:

.. code-block:: python

   >>> import math

This statement creates a module object named math. If you print the module object, you get some information about it:

.. code-block:: python
                
   >>> print math
   <module 'math' (built-in)>

The module object contains the functions and variables defined in the module. To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period). This format is called dot notation.

.. code-block:: python
                
   >>> ratio = signal_power / noise_power
   >>> decibels = 10 * math.log10(ratio)

   >>> radians = 0.7
   >>> height = math.sin(radians)

   
The first example uses log10 to compute a signal-to-noise ratio in decibels (assuming that signal_power and noise_power are defined). The math module also provides log, which computes logarithms base e.
The second example finds the sine of radians. The name of the variable is a hint that sin and the other trigonometric functions (cos, tan, etc.) take arguments in radians. To convert from degrees to radians, divide by 360 and multiply by 2 π:

.. code-block:: python

   >>> degrees = 45
   >>> radians = degrees / 360.0 * 2 * math.pi
   >>> math.sin(radians)
   0.707106781187
   
The expression math.pi gets the variable pi from the math module. The value of this variable is an approximation of π, accurate to about 15 digits.
If you know your trigonometry, you can check the previous result by comparing it to the square root of two divided by two:

.. code-block:: python
                
   >>> math.sqrt(2) / 2.0
   0.707106781187

   
Composition
-----------


So far, we have looked at the elements of a program—variables, expressions, and statements—in isolation, without talking about how to combine them.

One of the most useful features of programming languages is their ability to take small building blocks and compose them. For example, the argument of a function can be any kind of expression, including arithmetic operators:

.. code-block:: python
                
   x = math.sin(degrees / 360.0 * 2 * math.pi)
   
And even function calls:

.. code-block:: python
                
   x = math.exp(math.log(x+1))
   
Almost anywhere you can put a value, you can put an arbitrary expression, with one exception: the left side of an assignment statement has to be a variable name. Any other expression on the left side is a syntax error (we will see exceptions to this rule later).

.. code-block:: python
                
   >>> minutes = hours * 60                 # right
   >>> hours * 60 = minutes                 # wrong!
   SyntaxError: can't assign to operator


Adding new functions
--------------------

So far, we have only been using the functions that come with Python, but it is also possible to add new functions. A function definition specifies the name of a new function and the sequence of statements that execute when the function is called.
Here is an example:

.. code-block:: python
                
   def print_lyrics():
       print "I'm a lumberjack, and I'm okay."
       print "I sleep all night and I work all day."
       
``def`` is a keyword that indicates that this is a function definition. The name of the function is print_lyrics. The rules for function names are the same as for variable names: letters, numbers and some punctuation marks are legal, but the first character can’t be a number. You can’t use a keyword as the name of a function, and you should avoid having a variable and a function with the same name.
The empty parentheses after the name indicate that this function doesn’t take any arguments.

The first line of the function definition is called the header; the rest is called the body. The header has to end with a colon and the body has to be indented. By convention, the indentation is always four spaces (see Section 3.14). The body can contain any number of statements.

The strings in the print statements are enclosed in double quotes. Single quotes and double quotes do the same thing; most people use single quotes except in cases like this where a single quote (which is also an apostrophe) appears in the string.

If you type a function definition in interactive mode, the interpreter prints ellipses (...) to let you know that the definition isn’t complete:

.. code-block:: python
                
   >>> def print_lyrics():
   ...     print "I'm a lumberjack, and I'm okay."
   ...     print "I sleep all night and I work all day."
   ...
   
To end the function, you have to enter an empty line (this is not necessary in a script).
Defining a function creates a variable with the same name.

.. code-block:: python
                
   >>> print print_lyrics
   <function print_lyrics at 0xb7e99e9c>
   >>> type(print_lyrics)
   <type 'function'>
   
The value of print_lyrics is a function object, which has type 'function'.
The syntax for calling the new function is the same as for built-in functions:

.. code-block:: python
                
   >>> print_lyrics()
   I'm a lumberjack, and I'm okay.
   I sleep all night and I work all day.
   
Once you have defined a function, you can use it inside another function. For example, to repeat the previous refrain, we could write a function called repeat_lyrics:

.. code-block:: python
                
   def repeat_lyrics():
       print_lyrics()
       print_lyrics()
       
And then call repeat_lyrics:

.. code-block:: python
                
   >>> repeat_lyrics()
   I'm a lumberjack, and I'm okay.
   I sleep all night and I work all day.
   I'm a lumberjack, and I'm okay.
   I sleep all night and I work all day.
   
But that’s not really how the song goes.
   
Definitions and uses
--------------------

Pulling together the code fragments from the previous section, the whole program looks like this:

.. code-block:: python

   def print_lyrics():
       print "I'm a lumberjack, and I'm okay."
       print "I sleep all night and I work all day."

   def repeat_lyrics():
       print_lyrics()
       print_lyrics()

   repeat_lyrics()

This program contains two function definitions: print_lyrics and repeat_lyrics. Function definitions get executed just like other statements, but the effect is to create function objects. The statements inside the function do not get executed until the function is called, and the function definition generates no output.
As you might expect, you have to create a function before you can execute it. In other words, the function definition has to be executed before the first time it is called.


Parameters and arguments
------------------------

Some of the built-in functions we have seen require arguments. For example, when you call math.sin you pass a number as an argument. Some functions take more than one argument: math.pow takes two, the base and the exponent.

Inside the function, the arguments are assigned to variables called parameters. Here is an example of a user-defined function that takes an argument:

.. code-block:: python
                
   def print_twice(bruce):
       print bruce
       print bruce
       
This function assigns the argument to a parameter named bruce. When the function is called, it prints the value of the parameter (whatever it is) twice.
This function works with any value that can be printed.

.. code-block:: python
                
   >>> print_twice('Spam')
   Spam
   Spam
   
   >>> print_twice(17)
   17
   17
   
   >>> print_twice(math.pi)
   3.14159265359
   3.14159265359
   
The same rules of composition that apply to built-in functions also apply to user-defined functions, so we can use any kind of expression as an argument for print_twice:

.. code-block:: python
                
   >>> print_twice('Spam '*4)
   Spam Spam Spam Spam
   Spam Spam Spam Spam
   >>> print_twice(math.cos(math.pi))
   -1.0
   -1.0
   
The argument is evaluated before the function is called, so in the examples the expressions 'Spam '*4 and math.cos(math.pi) are only evaluated once.
You can also use a variable as an argument:

.. code-block:: python
                
   >>> michael = 'Eric, the half a bee.'
   >>> print_twice(michael)
   Eric, the half a bee.
   Eric, the half a bee.
   
The name of the variable we pass as an argument (michael) has nothing to do with the name of the parameter (bruce). It doesn’t matter what the value was called back home (in the caller); here in print_twice, we call everybody bruce.


Exercise
--------

Create a function with number argument (int). Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

hint (look bellow)

.. code-block:: python
                
   >>> 0 % 2
   0

   >>> 1 % 2
   1

   >>> 2 % 2
   0

   >>> 3 % 2
   1
                
   >>> 4 % 2
   0

   >>> 5 % 2
   1
