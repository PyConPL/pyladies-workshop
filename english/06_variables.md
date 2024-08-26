# Chapter 6. Variables

In this chapter:

You will learn what a **variable** is, how to define it, and how to use it.

## Variable

In the previous chapters, we performed various operations: we defined strings, multiplied numbers, etc. Each of these operations returned a result, which was immediately displayed on the screen. The text and numbers that we created in this way were stored in the computer's memory only for a moment and were immediately deleted from it after being displayed. Therefore, in subsequent operations, we could not use the results from previous operations.

To handle the issue of storing the result of an operation, we use **variables**. Instead of explaining how variables work, it is best to look at an example:

```python
>>> x = 7
>>> x
7
>>> 5 + x
12
```

Let's analyze what happened in the above example. At the beginning, we **defined a variable**, which means we assigned the result of some operation to a name. In this case, the operation is simply defining the number `7`, while the name is `x`. From this moment on, we could use the **variable** `x` in subsequent operations. If we simply type its name, we will get its **value**. We can also use it in another operation, for example by adding it to another number.

When defining variables, we can use other variables as well.

```python
>>> a = 10
>>> b = 5
>>> c = a + b
>>> c
15
```

Of course, in a real-life scenario, we name variables in such a way that they tell us what they represent.

```python
>>> net_price = 120
>>> vat_tax = net_price * 0.23
>>> gross_price = net_price + vat_tax
>>> gross_price
147.6
```

## Assignment

The operation `variable = value` is called **assignment**. As a result of the assignment, Python creates a *variable* that receives the *value*. If the value is an operation (e.g. addition), its result is first calculated and then assigned to the variable.


## Variable names

When creating a variable, we must first come up with a name for it. Above all, it should directly indicate the meaning of the variable. Thanks to this, as in the example above, we will be able to easily understand the program code.

In addition, Python imposes several restrictions on the characters we can use in variable names. Allowed characters include:

* letters from `a` to `z` (lowercase) and from `A` to `Z` (uppercase),
* numbers,
* symbol `_` (underscore).

All other characters are not allowed. Importantly, the name cannot start with a number!

:snake: Create variables `name` and `surname`, assign your name and surname to them. Then, based on them, create a variable `full_name` that will contain your name and surname separated by a space.

:snake: See what happens when you try to create a variable whose name starts with a number.


## Changing the value of a variable

At any time, we can change the value of a variable.

```python
>>> x = 'Ala ma kota'
>>> x
'ala ma kota'
>>> x = 'kot ma Alę'
>>> x
'kot ma Alę'
>>> x = x + '.'
>>> x
'kot ma Alę.'
```

## Variables and their methods

In previous chapters, we called various methods, such as `find` or `title`. Notice that methods that can be performed directly on an object can also be performed on a variable.

```python
>>> imie_nazwisko = 'jan kowalski'
>>> imie_nazwisko
'jan kowalski'
>>> imie_nazwisko.title()
'Jan Kowalski'
>>> imie_nazwisko
'jan kowalski'
>>> imie_nazwisko = imie_nazwisko.title()
>>> imie_nazwisko
'Jan Kowalski'
```

## :pushpin: Summary

In this chapter:

* we have learned what a variable is, how to define it, and how to use it.

---

:checkered_flag: Next chapter: [Functions](./07_functions.md) :checkered_flag:
