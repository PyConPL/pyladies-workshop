# Chapter 7. Functions

In this chapter:

You will learn how to define **functions**.


# What is a function

So far, we have learned what a *string*, *integer*, and *float* are, as well as how to use variables to store values between operations. This allows us to write a program that performs operations on data, for example processing text or performing calculations, and then displays the result on the screen. The more advanced problems we want to solve with our program, the more complex its code will be.

One way to write more understandable code is by defining functions. **Function** is a separate set of instructions that can be executed multiple times in a program. **Function definition** is a way of describing which operations should be included in the function.

For example, the following function returns a number squared:

The following is a function in Python that calculates the square of a number and returns the result.

```python
def square(number):
    result = number ** 2
    return result
```

* the word `def`,
* **name** of the function (in this example it's `square`),
* **list of arguments** enclosed in parentheses (here we have one argument `number`, but we can provide multiple, separating them with commas),
* colon.

Pay attention to spaces! In the entire header, there is only a space between the word `def` and the function name. If the function had multiple arguments separated by commas, we could insert spaces next to the commas to improve the readability of the code. Apart from these two cases, there should not be any more spaces in the header.

In the following lines after the header we have the **body of the function**. These are simply instructions that will be executed when we use the function. In the example above, the body contains two operations: squaring the value of the variable `number` and assigning it to the variable `result`, and returning the value of the variable `result`. **Returning** is the specification of what value should be the result of the given function. The word `return` is used for this purpose. If we type the name of the variable after it, its value will be the result. We can also return a result without assigning it to a variable beforehand.

```python
def square(number):
    return number ** 2
```

## Working with the editor

Before defining your first function, let's pause for a moment. So far, all operations have been performed in interactive mode, where we entered the code, pressed Enter and received the result. When we start working with functions, this approach may prove to be cumbersome. It will be much more convenient to switch to an **editor** now.

From now on, every example that does not start with `>>>` should be understood as code typed in the editor and run by clicking the "run" button.


## Definition and calling a function

Now copy the code of the function saved below into the editor. Pay special
attention to **indentation**. Each line of the function body must begin with
an indentation. Importantly, all of these indentations **must have the same
width**. This means that if you indent the first line by two spaces, then all
of the remaining lines until the end of the function must also be indented by
two spaces. As you will notice, the editor will automatically indent when you
press Enter after typing the header. If it does not do so, then the easiest
way to indent is by using the Tab key.

```python
def square(number):
    result = number ** 2
    return result
```

Press the "run" button now. If you don't notice any errors in the interactive mode window, it means that the function has been defined correctly. Now we can call it in interactive mode.

```python
>>> kwadrat(5)
25
>>> kwadrat(3) + kwadrat(1)
10
```

As you can see, to call a function, you just need to enter its name, followed by
the argument value in parentheses. If there are multiple arguments, they should be separated by commas.

:snake: Define a function named `circle_area` that takes an argument `radius` and returns the value of the equation `3.14 * (radius ** 2)`. Call it in the interactive mode window.

Call the `circle_area` function without an argument: `circle_area()`. Do you understand the message of the exception that was thrown?

Call the `circle_area` function with two arguments: `circle_area(2, 3)`.
Compare the exception message to the error from the previous task.


## Arguments

The function does not have to have any arguments, in this case we leave the parentheses in the header empty.

```python
def function_without_arguments():
    return 123
```

As we have mentioned, functions can take more than one argument.

```python
def sum(a, b):
    return a + b


def person(name, surname, title):
    name_surname = name + ' ' + surname
    return title + ' ' + name_surname.title()
```

We call these functions similarly to those with one argument.

```python
>>> function_without_arguments()
123
>>> sum(100, 45)
145
>>> sum(100, -20)
80
>>> person('jan', 'KOWALSKI', 'doctor')
'doctor Jan Kowalski'
```

:snake: Write a function `gross_price` that takes arguments `net_price` and `vat` and returns the gross value calculated according to the formula `net_price * (1 + vat)`.

:snake: Write a function `first_last_name` that takes arguments `first_name` and `last_name` and returns a string with the first and last name separated by a space. Make sure that each word in the string starts with a capital letter (use the `title` method). Then write a function `likes`, with arguments `first_name`, `last_name` and `what` and called like this: `likes('jan', 'kowalski', 'CAULIFLOWERS')` will return the string `'Jan Kowalski likes cauliflower'`. When writing the `likes` function, use the `first_last_name` function.


## Built-in functions

In addition to the functions that we can define ourselves, there are functions that are always available in the Python interpreter. We call them **built-in functions**. An example is the `len` function, which we mentioned in one of the previous chapters:

```python
>>> len('python')
6
```

In addition, we also have [67 other built-in functions](https://docs.python.org/3/library/functions.html). You will learn about some of them in the following chapters, and we have described a few others below.

### `str`

It takes any object as an argument and returns its representation as a string.

```python
>>> str(2017)
'2017'
```

:snake: Convert to string a negative number.

:snake: See what happens when you pass text as an argument to `str`.


### `int`

It takes any object as an argument and converts it to an integer.

```python
>>> int(' 123 ')
123
```

:snake: See what happens when you pass a number with a decimal part (float) to the `int` function, for example `3.14`.

:snake: See what happens if you pass a string with no numbers to `int`.

:snake: See what happens when you pass a string with both letters and numbers to `int`, for example `Ala has 2 cats`.


### `float`

It takes any object as an argument and converts it to a float.

```python
>>> float('3.14')
3.14
```

:snake: See how the `float` function will behave when called with:
an integer, a string with only letters, a string with only numbers.

## :pushpin: Summary

In this chapter:

* we have learned what a function is, how to define and call it,
* we have also familiarized ourselves with built-in functions such as `str`, `int`, and `float`.

---

:checkered_flag: Next chapter: [`print` function](./08_print_function.md) :checkered_flag:
