# Chapter 16. Standard library

In this chapter:

* you will learn what the **standard library** is,
* you will get to know the most important **modules** of the standard library.


## Library

In programming, we use the concept of a **library**, which refers to a collection of programs and tools for building them that we can use when writing our own programs. An example of a library could be a set of mathematical functions (e.g. trigonometric functions) that we can refer to in our code instead of defining them ourselves.


## Modules

In Python, programming libraries are accessible through **modules**. A module is simply code placed on a disk, in a location where Python can find it. This can be code written in Python, but there are ways to write modules in other programming languages. Python will find such code if it is placed in one of the predetermined directories.

Anyone can write their own module for Python. On the internet, we can find thousands of modules that are shared by different individuals and companies. We can download and use them to write programs. We can also create our own modules and share them with other users.

In order to use a module in our program code, we must **import** its name. We do this with the `import` statement. Once the module is imported, we can use the functions and variables defined within it. We do this by typing the module name, followed by a dot, and then the object name.

In the following example, we import a module called `math` and call the `sqrt` function, which returns the square root of a given number.

```python
import math
print(math.sqrt(9))
```

## The Python Standard Library

In addition to modules that users can write themselves, there is a set of modules that is always available in Python. This set is called the **standard library**. It contains dozens of modules, including tools for network communication, handling various file formats, mathematical calculations, etc.

The standard library is extensively documented on the [official Python website](https://docs.python.org/3/library/index.html).

## The most important modules

Discussing the entire standard library is a task that takes at least a few weeks, so during these workshops we will only mention a few of the most popular modules.

### [`math`](https://docs.python.org/3/library/math.html)

The `math` module contains dozens of mathematical functions that can be useful for simple calculations. Below, we have described several of them.

The `ceil` and `floor` functions return values rounded down and up, respectively.

```python
>>> math.ceil(3.5)
4
>>> math.floor(3.5)
3
```

The `sqrt` function returns the square root of a given number.

```python
>>> math.sqrt(25)
5.0
```

`pi` and `e` represent values of mathematical constants:

```python
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
```

:snake: Write a function that returns the value of the area of a circle with a given radius (according to the formula `PI * r^2`, where `r` is the radius).


### [`datetime`](https://docs.python.org/3/library/datetime.html)

The `datetime` module is a basic tool for working with dates and time. It contains objects `date`, `datetime`, and `timedelta`, which represent a date, date and time, and a time difference, respectively.

To get today's date, you need to call the `today` method on the `date` object.

```python
>>> datetime.date.today()
datetime.date(2024, 8, 29)
```

The object obtained in this way contains three **attributes**: `year`, `month`, and `day`, which correspond to the year, month, and day respectively.

```python
>>> today = datetime.date.today()
>>> today.year
2024
>>> today.month
8
>>> today.day
29
```

The `now` method on the `datetime` object will return the date and time that we have at the moment. In addition to the `year`, `month`, and `day` attributes, it also has `hour`, `minute`, `second`, and `microsecond`, which represent the hour, minute, second, and microsecond.

```python
>>> now = datetime.datetime.now()
>>> now
datetime.datetime(2017, 8, 13, 18, 53, 13, 366193)
>>> now.hour
18
>>> now.minute
53
>>> now.second
13
>>> now.microsecond
366193
```

Both types of objects can be displayed on the screen in a readable format:

```python
>>> print(today)
2017-08-13
>>> print(now)
2017-08-13 18:53:13.366193
```

To create a representation of any moment in time, simply call `date` or `datetime` and provide `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond` in order.

```python
>>> print(datetime.date(2010, 5, 10))
2010-05-10
>>> print(datetime.datetime(2020, 11, 23, 15, 7, 30))
2020-11-23 15:07:30
```

:snake: See what happens if you try to create an object `date` with a month outside the range of 1 to 12 or a date that doesn't exist, like April 31st.

:snake: See what will happen if you try to create a `datetime` object with an hour, minute, or second value outside of the allowable range (e.g. hour 26).

If we want to see the difference in time between two objects of type `datetime`, we can simply subtract them from each other.

```python
>>> a = datetime.datetime(2017, 8, 16, 17, 00)
>>> b = datetime.datetime(2017, 8, 16, 19, 00)
>>> diff = b - a
>>> diff
datetime.timedelta(0, 7200)
>>> diff.seconds
7200

In the above example, we received a `timedelta` object that has a `seconds` attribute with a value equal to the number of seconds between `a` and `b`.

If the difference is greater than one day, it will be divided into two values: `seconds` and `days`, which are seconds and days.

```python
>>> c = datetime.datetime(2017, 8, 16, 17, 00)
>>> d = datetime.datetime(2017, 8, 18, 15, 00)
>>> diff = d - c
>>> diff.seconds
79200
>>> diff.days
1
```

If we add one day and 79200 seconds to the date `c`, we will get `d`.

:snake: Write a function that takes two dates as arguments. If the second date is smaller than the first one, the function should return `None`. Otherwise, the function should return the number of seconds between the two dates. Note that the difference can be greater than one day. In this case, the number of days should be converted to seconds.


### [`random`](https://docs.python.org/3/library/random.html)

The `random` module is used to perform operations whose result is random:
generating random numbers, randomly selecting objects from a given range,
etc.

The `randint` function takes two integers as arguments and returns a randomly selected integer whose value is between the arguments.

```python
>>> random.randint(1, 100)
9
>>> random.randint(1, 100)
44
```

The `choice` function takes any sequence (list, tuple, string) as an argument and returns a randomly chosen element.

```python
>>> random.choice('ala ma kota')
'm'
>>> random.choice([9, 7, 5, 3])
7
>>> random.choice(('pycon', 'pl', '2024'))
'pl'
```

:snake: Write a function that takes any sequence as an argument and returns a *tuple* with three randomly selected elements from it.

### [`json`](https://docs.python.org/3/library/json.html)

The `json` module allows you to save Python objects (dictionaries and lists) as strings in the JSON (*JavaScript Object Notation*) format, which is commonly used in web services for exchanging data between the browser and the server.

To convert an object to a string, you need to call the `dumps` function.

```python
>>> json.dumps({'place': 'Ossa', 'date': '2017-08-16'})
'{"place": "Ossa", "date": "2017-08-16"}'
>>> json.dumps([2017, 8, 16])
'[2017, 8, 16]'
```

Do zamiany stringa na słownik lub listę służy funkcja `loads`:

```python
>>> json.loads('{"place": "Ossa", "date": "2017-08-16"}')
{'place': 'Ossa', 'date': '2017-08-16'}
>>> json.loads('[2017, 8, 16]')
[2017, 8, 16]
```

## What's next?

Above, we listed only a few of the most popular modules, so we encourage you to familiarize yourself with the rest of the standard library. It's worth starting with the official documentation, but you can also find plenty of articles online dedicated to using the standard library in everyday programming. Of course, you don't need to know it all to program freely in Python. Many of these modules have very specific uses and most programmers never use them. However, it's worth remembering that if you encounter a new problem, it's good to first search the standard library for a module that may be helpful.

## :pushpin: Summary

In this chapter:

* we learned what the **standard library** is and how to use it,
* we got to know the `math`, `datetime`, `random`, and `json` modules.


---

:checkered_flag: Next chapter: [Summarizon](./17_summarizon.md) :checkered_flag:
