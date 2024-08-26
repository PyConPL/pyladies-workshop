# Chapter 8. Lists

In this chapter:

* you will learn what **lists** are,
* you will get to know methods `append`, `pop`, `count`, `remove` and `index`,
* you will learn built-in functions `sum`, `max`, `min` and `sorted`.

## List

Lists accompany us every day. When we want to listen to music, we play a playlist. In the store, we look at the shopping list. When searching for something on the internet, we browse the list of results.

If we think about it further, we will notice that many other phenomena and things can be presented in the form of a list: a collection of books in a library, events from a certain period, tasks to be completed, a line of cars at a gas station, etc. List is a very important concept in programming, as it allows us to easily describe a set of objects that are arranged in a certain order: alphabetical, chronological, random, etc. Lists in Python are a powerful yet simple tool that is used almost every step of the way.

To define a list, you need to list objects (strings, integers) separated by commas in square brackets:

```python
>>> colors = ['blue', 'red', 'green', 'black']
>>> print(colors)
['blue', 'red', 'green', 'black']
```

In this way, we define an empty list:

```python
>>> empty_list = []
>>> print(empty_list)
[]
```

We can refer to individual list elements by entering their name, followed by the index number in square brackets. Remember that the numbering starts at zero!

```python
>>> print(colors[0])
blue
>>> print(colors[2])
green
```

To obtain the last element on the list, we can use the index `-1`:

```python
>>> print(colors[-1])
black
```

**Negative index** is a way to access elements of a list from the end.

```python
>>> print(colors[-2])
green
>>> print(colors[-3])
red
```

We can freely mix types of elements on the list.

```python
>>> numbers = ['one', 2, 'three', 4, 5]
```

The list may also contain other lists within it:

```python
>>> shades_of_red = ['crimson', 'red', 'burgundy']
>>> colors = ['green', shades_of_red, 'blue']
>>> print(colors)
['green', ['crimson', 'red', 'burgundy'], 'blue']
```

:snake: Write a function `element` that takes two arguments, a list and an index number (integer), and returns the element of the list located at the given index.

:snake: Write a function `last_element` that takes a list as an argument and returns its last element. Use the `element` function in it.


## List's methods

Lists, similar to strings, have many methods. Below you will find a description of several of the most useful ones.

### `append`

This method is used to add an element to a list.

```python
>>> numbers = [1, 3]
>>> print(numbers)
[1, 3]
>>> numbers.append(5)
>>> print(numbers)
[1, 3, 5]
>>> numbers.append(7)
>>> print(numbers)
[1, 3, 5, 7]
```

:snake: Write a function that takes a list as an argument and adds the same element at the end as it is at the very beginning.


### `pop`

The `pop` method does not take any arguments and returns the last element of the list, while also removing it from the list.

```python
>>> letters = ['a', 'b', 'c', 'd']
>>> print(letters)
['a', 'b', 'c', 'd']
>>> letters.pop()
'd'
>>> print(letters)
['a', 'b', 'c']
>>> letters.pop()
'c'
>>> letters.pop()
'b'
>>> print(letters)
['a']
```

:snake: Write a function that removes the last two elements from a list, and then adds to it the element that was last at the beginning.


### `count`

`count` takes one arbitrary object as an argument and returns the number of occurrences of that object in the list.

```python
>>> grades = [4, 3, 3, 5, 2, 3, 5, 4, 2, 4, 5, 4, 3, 3]
>>> grades.count(3)
5
>>> grades.count(4)
4
>>> grades.count(2)
2
```

### `remove`

The `remove` method takes any object as an argument and removes it from the list. If the object appears multiple times on the list, only its first occurrence is removed.

```python
>>> numbers = [10, 20, 25, 20, 10, 15]
>>> numbers.remove(20)
>>> print(numbers)
[10, 25, 20, 10, 15]
>>> numbers.remove(20)
>>> print(numbers)
[10, 25, 10, 15]
>>> numbers.remove(10)
>>> print(numbers)
[25, 10, 15]
```

:snake: Check what happens if we try to remove an element that is not on the list.

W:snake: rite a function that takes two arguments: a list and any other object. The function should remove the first occurrence of this object from the list and then add it to the end of the list. The function should return the number of occurrences of this element in the list.


### `index`

The `index` function takes one object as an argument and returns the position number at which this object is located on the list.

```python
>>> letters = ['r', 't', 'b', 'w', 'h']
>>> letters.index('t')
1
>>> letters.index('h')
4
```

:snake: Check what happens if we try to retrieve the index of an element that does not exist on the list.

## Lists and `len' function

Similarly to strings, we can check the length of a list using the built-in function `len`:

```python
>>> last_name_letters = ['K', 'o', 'w', 'a', 'l', 's', 'k', 'i']
>>> print(len(last_name_letters))
8
```


## Built-in functions `sum`, `min`, `max`, and `sorted`

There are several built-in functions that help us work with lists. Here we will describe some of them.

The first three are most helpful when we operate on lists where all elements are numbers. `sum` returns the sum of all elements, `min` returns the element with the smallest value, and `max` returns the one with the largest value.

```python
>>> measurements = [2, 4.25, 5.30, 3]
>>> sum(measurements)
14.55
>>> min(measurements)
2
>>> max(measurements)
5.3
```

:snake: Write a function that takes a list as an argument and prints to the screen the element with the highest value and the number of occurrences of that element in the list.

Another function is `sorted`, which takes a list and returns a sorted copy of that list.

```python
>>> results = [45.5, 47.2, 35.8, 41.0, 33.3]
>>> sorted_results = sorted(results)
>>> print(sorted_results)
[33.3, 35.8, 41.0, 45.5, 47.2]
>>> print(results)
[45.5, 47.2, 35.8, 41.0, 33.3]
```

:snake: Write a function that takes in a list as an argument, sorts it, and then returns its last element. (This way we will get our own version of the `max` function!)


## List snippets

Sometimes when operating on a list, we would like to use only a fragment of it, for example the first 10 elements or elements from the second to the fifth. Python is prepared for such a situation: it allows for creating a *slice* of a list. To create a slice, you need to enter the name of the list, followed by square brackets with the indexes of the first and last element of the slice separated by a colon.

For example, returning a fragment of the list from the second to the fourth element will look like this:

```python
>>> list_elements = [1, 2, 3, 4, 5, 6, 7]
>>> list_elements[1:4]
[2, 3, 4]
```

Remember that list indexes start at zero, and the element at the ending index (in this case: `5`) will not be included in the slice.

We can also omit the starting index. In this case, Python will return all elements from the beginning.

```python
>>> list_elements[:5]
[1, 2, 3, 4, 5]
```

If we omit the end index, we will get all elements until the end of the list.

```python
>>> list_elements[2:]
[3, 4, 5, 6, 7]
```

If the end index is a negative number, then the position of the last element in the slice will be counted from the end of the list.

```python
>>> list_elements[:-1]
[1, 2, 3, 4, 5, 6]
>>> list_elements[:-2]
[1, 2, 3, 4, 5]
```

Interestingly, we can also create fragments from strings:

```python
>>> text = 'ala ma kota'
>>> text[2:8]
'a ma k'
```

:snake: See what happens if the starting index is a negative number, or if the ending index is greater than the length of the list.

## :pushpin: Summary

In this chapter:

* we learned what lists are, how to define them, and how to refer to individual list elements.
* we also learned the most important list methods.
* we learned how to use built-in functions `len`, `sum`, `max`, `min`, and `sorted` on lists.

---

:checkered_flag: Next chapter: [`for` loop](./10_for.md) :checkered_flag:

