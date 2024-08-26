# Appendix 5. Tasks

This supplement contains a set of tasks that will help you consolidate the knowledge gained during the course. It will also teach you how to choose the appropriate types of data and operations depending on the problem you are facing.

When solving tasks, focus primarily on writing a functional program. Do not think about its "quality": how quickly it works or how nice the code looks. Start by solving the problem, and only then evaluate whether anything needs to be improved.


---


## 1. The `title` function

Write a function called `title` that will work like the `title` method on a string, but without using this method.

Example:

```python
>>> title('ala MA kOTA')
'Ala Ma Kota'
```


## 2. Grouping dictionaries

Write a function `group` that will group dictionaries according to the values for a selected key.

Example:

The following paragraph provides an example of how to translate a .md fragment into English while maintaining continuity with the previous paragraph.

```python
>>> fruits = [
...     {'name': 'apple', 'color': 'red'},
...     {'name': 'banana', 'color': 'yellow'},
...     {'name': 'lemon', 'color': 'yellow'},
...     {'name': 'pear', 'color': 'green'},
...     {'name': 'strawberry', 'color': 'red'}
... ]
>>> groups = group(fruits, 'color')
>>> for color, fruit_list in groups.items():
...     print(color, fruit_list)
...
red [{'name': 'apple', 'color': 'red'}, {'name': 'strawberry', 'color': 'red'}]
yellow [{'name': 'banana', 'color': 'yellow'}, {'name': 'lemon', 'color': 'yellow'}]
green [{'name': 'pear', 'color': 'green'}]
```

The function should take two arguments: a list of dictionaries and a key name. The result of the function should be a dictionary, where the keys are group names and the values are lists of dictionaries belonging to those groups.

## 3. The "delta compression" algorithm 

Write a `delta_compression` function that takes a **sorted** list of integers as an argument and returns the same list compressed using the following algorithm:

1. The first element of the output list is the same as the first element of the input list.
2. Each subsequent element of the output list is equal to the difference between the corresponding element of the input list and the element preceding it, that is `OUT[i] = IN[i] - IN[i-1]`.

Example:

```python
>>> we = [5, 7, 11, 21, 28, 39]
>>> delta_compression(we)
[5, 2, 4, 10, 7, 11]
```

## 4. Group and count

Write a function `group_and_count` that takes a list of two-element tuples as an argument, where the first element is a date (an instance of `datetime.date`) and the second is an integer, and calculates the sum of these numbers for each month that appears among these dates. The function should return a dictionary where the keys are tuples `(year, month)` and the values are the sums of the numbers.

Example:

```python
>>> x = group_and_count([
...     (datetime.date(2015, 1, 29), 10),
...     (datetime.date(2015, 1, 30), 12),
...     (datetime.date(2015, 1, 31), 10),
...     (datetime.date(2015, 2, 1), 9),
...     (datetime.date(2015, 2, 2), 9)
... ])
>>> print(x)
{(2015, 1): 32, (2015, 2): 18}
```

## 5. String Slicing

Write a function `cut` that takes two arguments: text and a number.
The function should return the text cut into fragments (a list), each
with a length equal to the number given in the argument. The last fragment may
be shorter than the required length.

Example:

```python
>>> cut('12345678', 3)
['123', '456', '78']
>>> cut('12345678', 5)
['12345', '678']
>>> cut('123', 4)
['123']
```

## 6. Counting words

Write a function that takes any text as an argument and returns a dictionary, where the keys will be all the words from that text, and the values will be the number of occurrences of those words in the text. The function should be case-insensitive (meaning 'Cat' and 'cat' should be treated as one word) and should ignore punctuation marks.

Example:

```python
>>> text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer soliciting ultricies eros, vitae eleifend ipsum sodales ut. Pellentesque libero ipsum, euismod eget volutpat nec, hendrerit vel turpis."
>>> count_words(text)
{'soliciting': 1, 'elit': 1, 'vel': 1, 'eleifend': 1, 'sodales': 1, 'eros': 1, 'sit': 1, 'nec': 1, 'consectetur': 1, 'pellentesque': 1, 'vitae': 1, 'eget': 1, 'hendrerit': 1, 'dolor': 1, 'turpis': 1, 'euismod': 1, 'integer': 1, 'lorem': 1, 'amet': 1, 'ipsum': 3, 'ut': 1, 'ultricies': 1, 'libero': 1, 'adipiscing': 1, 'volutpat': 1}
```
