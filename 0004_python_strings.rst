=======
Strings
=======


A string is a sequence
----------------------

A string is a sequence of characters. You can access the characters one at a time with the bracket operator:

.. code-block:: python
                
    >>> fruit = 'banana'
    >>> letter = fruit[1]

The second statement selects character number 1 from fruit and assigns it to letter. The expression in brackets is called an index. The index indicates which character in the sequence you want (hence the name).

But you might not get what you expect:

.. code-block:: python

    >>> print(letter)
    a

For most people, the first letter of 'banana' is b, not a. But for computer scientists, the index is an offset from the beginning of the string, and the offset of the first letter is zero.

.. code-block:: python

   >>> letter = fruit[0]
   >>> print(letter)
   b

So b is the 0th letter (“zero-eth”) of 'banana', a is the 1th letter (“one-eth”), and n is the 2th (“two-eth”) letter.

You can use any expression, including variables and operators, as an index, but the value of the index has to be an integer. Otherwise you get:

.. code-block:: python
  
   >>> letter = fruit[1.5]
   TypeError: string indices must be integers
   8.2  len

len is a built-in function that returns the number of characters in a string:

.. code-block:: python

   >>> fruit = 'banana'
   >>> len(fruit)
   6

To get the last letter of a string, you might be tempted to try something like this:

.. code-block:: python

   >>> length = len(fruit)
   >>> last = fruit[length]
    IndexError: string index out of range

The reason for the IndexError is that there is no letter in ’banana’ with the index 6. Since we started counting at zero, the six letters are numbered 0 to 5. To get the last character, you have to subtract 1 from length:

.. code-block:: python

   >>> last = fruit[length-1]
   >>> print(last)
   a

Alternatively, you can use negative indices, which count backward from the end of the string. The expression fruit[-1] yields the last letter, fruit[-2] yields the second to last, and so on.

Traversal with a for loop
--------------------------

A lot of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a traversal. 

.. code-block:: python

    for char in fruit:
        print(char)

Each time through the loop, the next character in the string is assigned to the variable char. The loop continues until no characters are left.

The following example shows how to use concatenation (string addition) and a for loop to generate an abecedarian series (that is, in alphabetical order). In Robert McCloskey’s book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs these names in order:

.. code-block:: python

   prefixes = 'JKLMNOPQ'
   suffix = 'ack'
   
   for letter in prefixes:
      print(letter + suffix)

The output is:

.. code-block:: python

   Jack
   Kack
   Lack
   Mack
   Nack
   Oack
   Pack
   Qack


A segment of a string is called a slice. Selecting a slice is similar to selecting a character:

.. code-block:: python

   >>> s = 'Monty Python'
   >>> print(s[0:5])
   Monty
   >>> print(s[6:12])
   Python

The operator [n:m] returns the part of the string from the “n-eth” character to the “m-eth” character, including the first but excluding the last. This behavior is counterintuitive, but it might help to imagine the indices pointing between the characters, as in the following diagram:

If you omit the first index (before the colon), the slice starts at the beginning of the string. If you omit the second index, the slice goes to the end of the string:

.. code-block:: python

   >>> fruit = 'banana'
   >>> fruit[:3]
   'ban'
   >>> fruit[3:]
   'ana'

If the first index is greater than or equal to the second the result is an empty string, represented by two quotation marks:

.. code-block:: python

   >>> fruit = 'banana'
   >>> fruit[3:3]
   ''

An empty string contains no characters and has length 0, but other than that, it is the same as any other string.

Exercise 3   Given that fruit is a string, what does fruit[:] mean?


Counting
--------

The following program counts the number of times the letter a appears in a string:

.. code-block:: python

   word = 'banana'
   count = 0
   for letter in word:
      if letter == 'a':
         count = count + 1
   print(count)


String methods
--------------

A method is similar to a function—it takes arguments and returns a value—but the syntax is different. For example, the method upper takes a string and returns a new string with all uppercase letters:

Instead of the function syntax upper(word), it uses the method syntax word.upper().

.. code-block:: python

   >>> word = 'banana'
   >>> new_word = word.upper()
   >>> print(new_word)
   BANANA

This form of dot notation specifies the name of the method, upper, and the name of the string to apply the method to, word. The empty parentheses indicate that this method takes no argument.

A method call is called an invocation; in this case, we would say that we are invoking upper on the word.

As it turns out, there is a string method named find that is remarkably similar to the function we wrote:

.. code-block:: python

   >>> word = 'banana'
   >>> index = word.find('a')
   >>> print(index)
   1

In this example, we invoke find on word and pass the letter we are looking for as a parameter.
Actually, the find method is more general than our function; it can find substrings, not just characters:

.. code-block:: python

   >>> word.find('na')
   2

It can take as a second argument the index where it should start:

.. code-block:: python

   >>> word.find('na', 3)
   4

And as a third argument the index where it should stop:

.. code-block:: python

   >>> name = 'bob'
   >>> name.find('b', 1, 2)
   -1

This search fails because b does not appear in the index range from 1 to 2 (not including 2).

The word ``in`` is a boolean operator that takes two strings and returns True if the first appears as a substring in the second:

.. code-block:: python

   >>> 'a' in 'banana'
   True
   >>> 'seed' in 'banana'
   False


String comparison
-----------------

The relational operators work on strings. To see if two strings are equal:

.. code-block:: python

   if word == 'banana':
      print('All right, bananas.')

Other relational operations are useful for putting words in alphabetical order:

.. code-block:: python

   if word < 'banana':
      print('Your word,' + word + ', comes before banana.')
   elif word > 'banana':
      print('Your word,' + word + ', comes after banana.')
   else:
      print('All right, bananas.')

Python does not handle uppercase and lowercase letters the same way that people do. All the uppercase letters come before all the lowercase letters, so:
Your word, Pineapple, comes before banana.
A common way to address this problem is to convert strings to a standard format, such as all lowercase, before performing the comparison. Keep that in mind in case you have to defend yourself against a man armed with a Pineapple.
