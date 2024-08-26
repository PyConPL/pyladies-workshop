# Chapter 14. `None`

In this chapter:

* you will learn what **`None`** is.


## `None`

In Python, there is one particular value that does not represent any known type so far: **`None`**. It is not a number, string, or anything else you will learn while studying this language. `None` is a unique value that represents a separate type. It was created for the purpose of allowing the programmer to define "nothing". Why? It turns out that there are situations where you want to explicitly indicate that a particular operation did not return any significant information. In such situations, you can use the value `None`. Note that the mere use of this value is so exceptional that it suggests that some special circumstances have arisen.

An example of using `None` can be dividing by 0. As we know, this mathematical operation is not allowed. Now, let's imagine that we are writing a function that takes two numbers as arguments and returns the result of dividing one by the other.

```python
def divide(dividend, divisor):
    return dividend / divisor
```

What will happen if the `divisor` argument is equal to `0`? We will receive an error.

```python
>>> divide(3, 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in podziel
ZeroDivisionError: division by zero
```

To prevent this, we can check the value of the argument before performing division and return `None` if necessary, signaling that we cannot calculate the result.

Translate:

```python
def divide(dividend, divisor):
    if divisor == 0:
        return None
    return dividend / divisor
```

Now we can easily recognize when the function encounters a non-standard call.

```python
>>> result = divide(4, 2)
>>> print(result)
2.0
>>> result = divide(5, 0)
>>> print(result)
None
```

## Default function value

Let's write a simple function that takes an argument and prints it on the screen:

Translate this .md fragment to English, keeping it in line with the previous paragraph.

```python
def print_something(something):
    print(something)
```

Calling the function will result in the expected consequences.

```python
>>> print_something(123)
123
>>> print_something('ala ma kota')
ala ma kota
```

We see that the function body has been executed, but what value was returned? In other words, what happens if we do not use the `return` statement? The answer is: the function will return `None`.

```python
>>> result = print_something('abc')
abc
>>> print(result)
None
```

The same thing happens if we use the `return` statement without providing any value:

Translate this .md fragment to English, keeping in line with the previous paragraph.

```python
def print_something(something):
    print(something)
    return
```

The effect will be the same as when we do not use `return`.

```python
>>> result = print_something(3.14)
3.14
>>> print(result)
None
```

There is no magic behind this behavior: the creators of Python simply adopted the convention that a function returns "nothing" by default, and this value will be represented by `None`.


## `is` operator

Now that we know that functions can return `None`, how can we use this? We can, for example, check the returned value in an `if` statement.

```python
def name_surname(name, surname):
    if name != '' and surname != '':
        return name + ' ' + surname

def username(name, surname, email):
    full_name = name_surname(imie, nazwisko)
    if full_name == None:
        return email
    else:
        return full_name
```

In the above example, the `username` function returns the full name of the user based on their first name, last name, and email address. If the first and last name are provided, the full name is returned, otherwise only the email address is returned. Checking if the full name is provided is saved in the `if full_name == None` statement.

The `if variable == None` instruction is correct, however in general it may not always work. This is because when creating more advanced data structures in Python (which will not be discussed during these workshops), we can change the comparison behavior, resulting in a different return value for the `==` operator. If we do this carelessly, it may turn out that an `if` operation works differently than expected. We can get out of this situation by using the **`is` operator** instead.

```python
if full_name is None:
    return email
```

In this way, our code will be insensitive to modifications of the behavior of the `==` operator.

When should you use `is`? Use this operator whenever you compare a value to `None`. For now, it won't make a difference, but this way you will acquire a good habit that will prove useful in the future.

:snake: Write a function that takes a list as an argument and returns a list containing all elements from the argument, except for values equal to `None`.

## :pushpin: Summary

In this chapter:

* we learned about `None`,
* we found out that when comparing values to `None`, we should use
the `is` operator.


---

:checkered_flag: Next chapter: [`while` loop](./15_while_loop.md) :checkered_flag:
