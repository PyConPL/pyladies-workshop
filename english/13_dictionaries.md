# Chapter 13. Dictionaries

In this chapter:

You will learn what a **dictionary**, **key**, and **value** are,
you will learn how to define dictionaries and perform operations on them,
you will discover the most common uses of dictionaries.


## What is a dictionary?

Many situations you will encounter while writing programs can be described as a set of keys and their corresponding values. An example from everyday life is an encyclopedia, where the keys are different entries and the values are definitions explaining those entries. You can go further and say that the internet is a collection of addresses (e.g. `pl.pycon.org`) and the web pages that are hidden behind them.

This perspective on the reality surrounding us is very convenient, as it allows us to describe complex phenomena in a systematic, easy-to-understand manner. That is why many programming languages offer tools for creating such data structures. In the case of Python, these are **dictionaries**.

A dictionary, abbreviated as "dict", is a collection of **keys** and their corresponding **values**. The name "dictionary" is not accidental, as it refers to the formula in which we assign definitions to a set of words.


## Definition of dictionary

We define a dictionary by listing key-value pairs separated by commas, enclosed in curly braces. Each pair consists of two values separated by a colon.

```python
age = {'Marcin': 23, 'Agata': 17, 'Marta': 46}
```

To create an empty dictionary, simply use empty curly brackets:

```python
d = {}
```

The values in a dictionary do not have to be of the same type, one can be a number, another a string, etc.

```python
d = {'number': 123, 'another number': 12.34, 'list': ['Ala has a cat']}
```

Keys can also be numbers.

```python
d = {15: 'Ala ma kota', 'Kot ma alę': 3.14}
```

The dictionary can also be an element of the list.

```python
l = [{'a': 1, 'b': 2}, 3, 4]
```

When we print the dictionary on the screen, we will see its entire contents.

```python
>>> d = {'a': ['x', 9, 'z'], 'b': 2, 'c': 'Ala ma kota'}
>>> print(d)
{'a': ['x', 9, 'z'], 'b': 2, 'c': 'Ala ma kota'}
```


## Operations on dictionaries

Once we define a dictionary, we can perform a variety of operations on it.


### Downloading the value of an element

To obtain a value for a given key, you must enter the name of the dictionary, followed by the key name in square brackets.

```python
>>> d = {'a': 1, 'b': 2}
>>> print(d['a'])
1
>>> print(d['a'] + d['b'])
3
```

:snake: See what happens if you retrieve a value for a key that does not exist in the dictionary.

:snake: Write a function that takes two arguments, a list of dictionaries and a key, and returns a list of values under that key from each dictionary in the list.


### Defining an element

At any time, we can define the value of a key in a dictionary. To do this, we need to refer to the specific key and assign a value to it.

```python
>>> d = {'a': 1}
>>> d['b'] = 2
>>> d[5] = ['list of', 'elements']
>>> print(d)
{'a': 1, 'b': 2, 5: ['list of', 'elements']}
>>> print(d[5])
['list of', 'elements']
```

If the given key already exists, its value will be overwritten.

```python
>>> d = {'a': 1}
>>> print(d['a'])
1
>>> d['a'] = 2
>>> print(d['a'])
2
```

### Removing an element

We can delete any key from the dictionary using the `del` instruction:

```python
>>> d = {'a': 1, 'b': 2}
>>> del d['a']
>>> print(d)
{'b': 2}
```

:snake: See what happens if you try to delete a key that does not exist in the dictionary.

### Iterating through keys and values

In one of the previous chapters, we talked about iteration in the context of a list, meaning "going through" its elements. We used a `for` loop for this purpose. If we perform the same operation on a dictionary, we will go through its keys.

```python
for key in dictionary:
    print(key)
```

:snake: Write a function that takes a dictionary as an argument and iterates through its keys, printing each one.

In a similar way, we can iterate through only the values of a dictionary. This is done using the `values` method.

```python
start_list = {1: 'Winnie the Pooh', 2: 'Piglet', 3: 'Tigger'}
for competitor in start_list.values():
    print(competitor)
```

:snake: Write a function that takes a dictionary as an argument and returns the sum of all values in the dictionary. We assume that the values are always numbers.

The dictionary also has a `items` method, which allows us to iterate simultaneously over the keys and values of the dictionary.

```python
start_list = {1: 'Winnie the Pooh', 2: 'Piglet', 3: 'Tigger'}
for number_start, competitor in start_list.items():
    print(number_start, ':', zawocompetitordnik)
```

Note that this time we defined two variables in the `for` loop:
`starting_number` and `player`. This is not specific to dictionaries,
but rather another feature of this loop. If the loop iterates through a list,
where all elements are sequences (lists or tuples),
we can immediately **unpack** all elements of these sequences into
variables:

```python
lists = [['a', 'Apple', 'Argentina'], ['b', 'Banana', 'Brasil']]
for letter, fruit, country in lista:
    print(fruit)
```

Returning to dictionaries, in our case the first element of each sequence is the key, and the second is the value for that key.

:snake: Write a function that takes two arguments, a dictionary and a value, and returns the name of the key whose value is equal to the argument value.


## Nesting dictionaries

The value in the dictionary can be any object, including another dictionary. This allows us to easily create complex data structures.

```python
>>> auto = {}
>>> auto['color'] = 'red'
>>> auto['engine'] = {'capacity': 1600, 'power': 130}
>>> print(auto)
{'color': 'red', 'engine': {'capacity': 1600, 'power': 130}}
```


## The "length" of a dictionary

When we first mentioned the `len` function, we said that it is used to check the length of objects. Each type of object (string, list, etc.) may interpret the concept of length differently. For strings, it refers to the number of characters, for lists it refers to the number of elements, etc. Dictionaries also have their own "length": it is equal to the number of keys.

```python
>>> print(auto)
{'color': 'red', 'engine': {'capacity': 1600, 'power': 130}}
>>> len(auto)
2
```


## What can we use dictionaries for?

A dictionary is a very versatile data structure, which makes it useful for many applications.

* representation of objects and their attributes (as in the example above),
* mapping of one value to another (as in a real dictionary, where we map words from one language to another),
* storing multiple related values in one place (e.g. keys are movie titles and values are their directors).

:snake: Choose one of the above dictionary applications. Write a function `set` that takes three arguments, a dictionary, a key, and a value, and sets the given value in the dictionary under the given key. Write a function `get` that takes two arguments, a dictionary and a key, and returns the value of the dictionary under the given key. Using these functions, fill the dictionary with data appropriate for the chosen application and retrieve this data.

## :pushpin: Summary

In this chapter:

* we learned how to create dictionaries and perform operations on them, including iterating through them,
* we also found out that the `len` function returns the number of keys in a dictionary,
* we got to know the most commonly used applications of dictionaries.


---

:checkered_flag: Next chapter: [`None`](./14_none.md) :checkered_flag:
