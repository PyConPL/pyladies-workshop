# Summary

We are reaching the end of the course, but it's not the end of the workshops yet! There are still additional chapters waiting for you - you will find them in the "Add-ons" section below the table of contents. In addition, the mentors have a handful of tasks for you. You can also take this opportunity to ask the mentors as many questions as time allows - that's one of the reasons why we organized these workshops!


## What we didn't talk about

Unfortunately, the time for the workshops is limited, so the range of topics we covered is not exhaustive. You already know the basics of Python. You can now write your own programs and reading others' will no longer be so difficult. However, at this stage, you will often come across code that you do not understand. Or maybe you already know about topics that seem interesting, but you do not know how to start. That is why we have prepared a list of topics for you, which you can treat as a continuation of these workshops. This list is not exhaustive, but it will certainly help you to get to know Python even better. In each point, we have included a link to a page that explains the given topic.

* [More about exceptions and how to handle them](https://docs.python.org/3.12/tutorial/errors.html)
* [Classes, or object-oriented programming](https://docs.python.org/3.12/tutorial/classes.html)
* [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
* [Generators](https://docs.python.org/3/glossary.html#index-17)
* [List comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Finally... `dir`

To conclude, we will show you one more, very useful built-in function. It is called `dir`, it takes any object as an argument and returns a list of all methods and attributes of that object.

```python
>>> d = {'a': 1}
>>> dir(d)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

In the example above, you will definitely recognize a few familiar names, such as `items` or `values`, but as you can see, dictionaries offer much more. Pay attention to names starting and ending with a double underscore. These are the names of attributes and methods that are not intended for object users. They are usually things used only within a specific object. Of course, they can still be used - they just may not be useful to us, so it is worth exploring the remaining names.

What to do with such a list now? If a name seems obvious, we can simply try to use it - in the worst case scenario, we will receive an error message explaining what we did wrong. We can also - and we recommend it - use the `help` function, which will display the documentation of a given object.

```python
help(d.update)
```

## :checkered_flag: End

Thank you for participating in the workshops! Once again, we encourage you to talk to the mentors - they will gladly answer all your questions and explain any topics that may be unclear.

If you have any comments about this course, please share them by writing to the authors or passing them on to mentors. Your opinion is very important to us!

![Programming is fun again](https://imgs.xkcd.com/comics/python.png)
