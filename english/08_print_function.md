# Chapter 8. `print` function

In this chapter:

* you will learn about the built-in function `print`.


## Printing text on the screen

When we were using the interactive mode and wanted to print something on the screen, all we had to do was enter an expression and press Enter.

```python
>>> 2 + 2
4
>>> x = 'PyLadies'
>>> x
'PyLadies'
```

We were able to do this because interactive mode works in this way: it performs an operation and displays its result. However, Python programs are usually more complex and it often happens that we want to see more than just the result of the last operation. For example, when we write a program that processes a text file and we want it to print something on the screen for each line of text. In such cases, the built-in function `print` comes in handy.


## `print`

This function takes any number of arguments and prints them all to the screen, separating them with spaces:

```python
>>> print(2024)
2024
>>> print('PyCon PL', 2024)
PyCon PL 2024
```

In addition, variables can also be passed to `print`.

```python
>>> temperature = 24
>>> print('Temperature:', temperature, 'degrees')
Temperature: 24 degrees
```

:snake: Write a function that takes an argument `year_of_birth`, prints the text `You are X years old`, where `X` is the age in 2017, and returns that age.


## Formatting strings

At this point, it's worth going back to strings and talking about one more very useful method: `format`. It is used for **formatting strings**, which means "inserting" variable values into them. Take a look at the example below:

```python
>>> 'ala {} a cat'.format('has')
'ala has a cat'
```

As you can see, calling the `format` method caused the pair of characters `{}` to be replaced with function arguments. In a similar way, we can insert any number and type of objects.

```python
>>> width = 110
>>> height = 50.5
>>> unit = 'mm'
>>> '{}x{} {}'.format(width, height, unit)
'110x50.5 mm'
```

The capabilities of the `format` method are not limited to simply inserting values into a string. The [Python documentation](https://docs.python.org/3.12/library/string.html#formatspec) provides a detailed description of this function. It is worth taking a look at the examples provided there.

:snake: See what happens if the number of arguments of the `format` method is __less__ than the number of occurrences of `{}` in the string.


## :pushpin: Summary

In this chapter:

* we have learned about the `print` function and the `format` method.

---

:checkered_flag: Next chapter: [Lists](./09_lists.md) :checkered_flag:
