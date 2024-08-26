# Chapter 11. Short description

In this chapter:

* you will learn what a **tuple** is.


## Tuple

When reading code of programs written in Python, you will quickly come across something that may seem very similar to a list:

```python
currencies = ('EUR', 'PLN', 'USD')
```

The above example is a definition of a **tuple**. At first glance, it differs from a list only in that it uses round brackets instead of square brackets. However, a tuple has one important characteristic that sets it apart from a list: it cannot be modified. This means that once a tuple is created, elements cannot be added, removed, or changed. Therefore, we will not find methods such as `append` or `remove` in a tuple. However, we can successfully refer to individual elements using their indexes.

```python
>>> currencies[1]
'PLN'
```

This means that we can also iterate through a tuple using a `for` loop. If we pass a tuple to the `len` function, we will get the number of its elements.

:snake: Write a function that takes a tuple as an argument and returns a list with exactly the same elements.


## Usage of tuples

At first glance, a tuple may seem completely unnecessary. Why do we need such a list that cannot be modified? However, in many cases, we need exactly something like this. A good example is a set of currency names. Imagine that we are writing a program to convert monetary values between different currencies. In our program, exchange rates will change, but the currencies themselves will remain the same. Therefore, we can define them in a tuple, thus protecting ourselves from modifying the set of currencies, which would be undesirable. Even if we want to add another currency in the future, it will be easier to release a new version of the program than to risk modifying the set, which should remain unchanged.

There are more similar examples and by reading the code of various programs, you will quickly realize that tuples are more useful than it may seem.

## :pushpin: Summary

In this chapter:

* we learned what a tuple is and what operations we can perform on it.


---

:checkered_flag: Next chapter: [True and false](./12_true_and_false.md) :checkered_flag:
