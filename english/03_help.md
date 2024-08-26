# Chapter 3. The `help` function

In this chapter:

* you will learn about the `help` function.


## Python Help

Even the best programmer will never remember all the functions and methods that Python offers. During this training, you will learn many of them, but in a few days you will forget how they work. Don't worry, the creators of Python have thought about it...


## The documentation of method in Python

Every method defined in Python has **documentation**, which describes its functionality in a few words. To read this documentation, you need to call the `help` function, for example:

```python
>>> help('some string'.find)
Help on built-in function find:

find(...)
    S.find(sub [,start [,end]]) -> int

    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.

    Return -1 on failure.
```

Documentation is not always written in simple language, but don't be discouraged. It's worth getting familiar with it from the very beginning. Read the above fragment again, and we will explain what each part means.

The documentation shows all the arguments that a given method takes.
This information is contained in the line "S.find(sub [,start [,end]])".
Furthermore, the documentation informs about the type of result that is returned and briefly explains what this method does. This allows us to quickly remind ourselves about it.

Note that in this example we did not open parentheses after the method name `find`, and therefore we did not provide any arguments. This way, instead of calling this method, we simply used its name. When we pass such a name to the `help` function, Python will show us the documentation for that method.

:snake: Use the `help` function and read the documentation for the `replace` and `count` methods as well as the `len` function.


## :pushpin: Summary

In this chapter:

* we learned about the `help` function and found out that it's worth using when we don't understand a method or can't remember how it works.


---

:checkered_flag: Next chapter: [Numbers](./04_numbers.md) :checkered_flag:
