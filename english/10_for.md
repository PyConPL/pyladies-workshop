# Chapter 10. `for` loop

In this chapter:

* you will learn what **iteration** and **loop** are,
* you will get to know the `for` loop.


## Iteration

When we operate on a list, we often want to "iterate" through all of its elements one by one and perform some operation on each of them. This type of "iteration" is called **iteration**. In Python, to get each element of the list in order, we can of course use indexes:

```python
>>> dates = ['15/07/2017', '16/07/2017', '17/07/2017']
>>> print(dates[0])
15/07/2017
>>> print(dates[1])
16/07/2017
>>> print(dates[2])
17/07/2017
```

However, this approach is inconvenient when the list is very long.
But what if we don't even know how long the list is? These problems can be solved using **loops**, which are instructions that execute certain operations until a condition is met. With loops, we can, for example, iterate, meaning perform operations on each element of the list until we reach the end of the list.

## For loop

Loops have many uses, but iteration is one of the most commonly encountered. That is why Python has a `for` loop, which is used precisely for this purpose. Let's look at an example:

```python
departure_hours = ['7:30', '13:45', '16:10']
for hour in departure_hours:
    print(hour)
```

Copy and execute the above code in the editor. In the interactive mode window, you will see that the `print` function was executed for each element on the list, displaying it on the screen. This happened because Python went through all the elements on the `departure_hours` list and assigned their values to the `hour` variable, then executed the `print` operation.

The definition of a loop starts with the word `for`, then the name of the
variable to which the values of each element will be assigned, followed by
the word `in`, the name of the list, and a colon. In the following lines,
there are operations that will be performed for each element.
Remember that each operation must be indented in the code in the same way.
Their width does not matter, it is important that they are the same.

If the loop is inside a function, then the indentation inside the `for` should be increased by the function's indentation width.

```python
def print_elements(list_elements):
    for element in list_elements:
        print(element)
```

:snake: Write a function that takes a list of numbers as an argument and prints out the squared value of each of them on the screen.

:snake: Write a function that takes a list of strings and returns a new list, on which all these strings will be written in uppercase (use the `upper` method).

## `For` and strings

The `for` loop is very versatile: you can also use it on a string. In this case, its elements will be individual letters.

```python
for letter in 'ala has a cat':
    print(letter)
```

:snake: Write a function that takes a string as an argument and prints each letter along with the number of occurrences of that letter in the string (use the `count` method).


### The `split` method

We can also iterate through words. To do this, we use the `split` method.

```python
for word in 'ala has a cat'.split():
    print(slowordwo)
```

In fact, the `split` method has much broader application. If we provide a character as an argument, then the string will be divided at the locations where this character appears.

```python
>>> text = '2015,2016,2017'
>>> text.split(',')
['2015', '2016', '2017']
```

If no argument is passed, the string will be split at spaces.

```python
>>> 'ala has a cat'.split()
['ala', 'has', 'a', 'cat']
```

:snake: Write a function that takes a string as an argument and prints all of its words, each on a separate line.


## `range`

It is worth mentioning the built-in function `range` in this place. It takes two integers as arguments: the beginning and end of a numerical range that it returns. We can then iterate through such a range and the elements will be consecutive integers.

```python
for num in range(10, 20):
    print(num)
```

In the above example, we print out integers from 10 to 19. The number that we specified as the end of the range is not included in it.

Interestingly, we can only provide one argument, which is then treated as the end of the range, while 0 is taken as the start. The next example shows how to print numbers from 0 to 99.

```python
for num in range(100):
    print(num)
```

Write a function that takes one argument named `limit` and returns a list of values from 0 to `limit` squared.


## :pushpin: Summary

In this chapter:

* we learned the concepts of *iteration* and *loop*,
* we learned how to use the `for` loop,
* we found out that the `for` loop also works on strings, and that
strings have the `split` method,
* we learned about the built-in function `range`.


---

:checkered_flag: Next chapter: [Tuples](./11_tuples.md) :checkered_flag:
