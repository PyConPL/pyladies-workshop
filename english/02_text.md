# Chapter 2. Text

In this chapter:

You will learn what a `string` is and what can be done with it,
you will learn how to write programs that display text.

## String

Almost every program generates some text. Smartphone applications display messages about received messages. Web applications return the content of web pages. Servers save information on their disk about how they are functioning. Text is the basis of communication between a computer and a human. That is why we will start learning programming with operations on text, or, as we say in programming jargon, on **strings**.

String, or a string of characters, is simply a sequence of letters, numbers, dots,
commas, etc. To define a string in Python, simply enclose some text between the characters `'` (single apostrophe):

```python
>>> 'PyLadies 2024'
```

In the above string, there are uppercase and lowercase letters, spaces, and numbers. There are [thousands of characters](https://en.wikipedia.org/wiki/Unicode) that you can use.

:snake: Before you continue, try to create strings on your own with the following information: Your first and last name, name of the town where you come from, title of your favorite movie or book.


## Apostrophes

The example we used a moment ago shows a string enclosed in single quotation marks, which is `'`. If you want, you can use the character `"`. For Python, this does not matter. What is important, however, is that the same apostrophe is found on both sides of the string: if you start with a double one, you must end with a double one. The same goes for single ones.


## String operations

Now, when you know how to define a string, let's try to perform an operation on it. By "operation" we mean transforming one string into another string, for example:

```python
>>> 'Winnie the Pooh'.lower()
'winnie the pooh'
```

(Note the lack of spaces around the period!)

In this example, we performed two operations: we defined a string `'Kubuś Puchatek'` and **called the method** `lower`. A method is simply an operation that can be performed on an object. In this case, our object is a string and the method is `lower`, which created a new string where all capital letters were changed to lowercase.

In Python, strings have many other methods, for example:

* `upper` - opposite of `lower`,
* `title` - changes the first letter of each word from lowercase to uppercase,
* `strip` - removes spaces from the left and right side of the string (if they exist).

:snake: Now try out these methods in such a way that you can see the effects of their operation. Test them on the strings that we created in the previous exercise.


## What are string operations used for?

When writing programs, we often have to deal with strings that come from sources over which we have no control. For example, information from a form filled out by a user, or data read from a file. In all of these cases, we process strings whose structure we know nothing about. Operations help us transform strings into the desired format, or search for information within them.

A good example is a first and last name. Imagine that you are creating a program that asks the user for their first and last name. You want to save this data in the format `First Name Last Name`, so that each word starts with a capital letter. However, the user may enter `jan kowalski` or `JAN KOWALSKI` in the form. In both cases, you will get strings in a different format than you expect. You can handle this by using the `title` method, which will convert both values to `Jan Kowalski`.


## Operations with arguments

Some operations require additional options to be provided. For example:

```python
>>> 'Winnie the Pooh'.find('ni')
3
```

The `find` method searches for the given string in a string and returns the index of the character in which the string begins. Note that the characters are numbered starting from zero.

```
W i n n i e   t h e ...
0 1 2 3 4 5 6 7 8 9 ...
```

We called the `find` method, giving it the string `'Pu'`. This string is located inside the string `'Winnie the Pooh'` and starts at character number 6, which is why we saw this number on the screen.

The values that we have to provide when calling a method (e.g. `'Pu'` from the example) are called **arguments**. Some methods do not take any arguments, but there are also those that require one or more to be given. If a method takes multiple arguments, they must be separated by commas.


## `find`, `replace`, `count`

We will not go through all the methods that the string has right now, but there are three worth knowing from the very beginning, as they are often used.

### `find`

We just learned about `find`: it takes a string as an argument and searches for it in the string on which we performed the operation. If the substring is found, we receive the index of the first character. Otherwise, we receive `-1`.

This method is useful when we are looking for a specific phrase and want to check if a given string contains it. For example, when we want to find out if our user's name is "Nowak".

```python
>>> 'Anna Nowak'.find('Nowak')
5
>>> 'Jan Kowalski'.find('Nowak')
-1
>>> 'Tomasz Nowak'.find('Nowak')
7
```

In the above example, if the value returned by `find` is different than `-1`, it means that the user's last name matches.

Note that capitalization matters:

```python
>>> 'Piglet'.find('Pig')
0
>>> 'Piglet'.find('pig')
-1
>>> 'piglet'.find('Pig')
-1
```

This method is also useful when we are certain that a given string contains the desired character string, but we need to check at which exact position.

For example, we can find out which letter of the alphabet is the letter `r`.

```python
>>> 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż'.find('r')
23
```

Note that the letter `a` is at position `0`, so the letter `r` is not actually the twenty-third, but the twenty-fourth letter of the alphabet. This example shows how important it is to correctly interpret the information returned by programs.

:snake: Choose a few paragraphs (2 or more) from this page and for each of them: copy its content and use it to define a string, then call the `find` method on it to check if it contains the string `and`.

### `replace`

The `replace` method takes two arguments: strings `a` and `b`. When we call this method on a certain string, all occurrences of string `a` in that string will be replaced with string `b`.

For example, you can replace all spaces with a `-` character.

```python
>>> 'Ala has a cat'.replace(' ', '-')
'Ala-has-a-cat'
```

Or replace entire words:

```python
>>> Ala has a cat'.replace('cat', 'dog')
'Ala has a dog'
```

Another example of using this method is removing a character from a string. You can do this by passing an empty string as the second argument:

```python
>>> 'Jan Kowalski'.replace('Kowalski', '')
'Jan '
```

:snake: Enter your first and last name in interactive mode, and then use the `replace` method to change your name to the name of one of the workshop participants sitting next to you.

### `count`

`count` takes one string as an argument and returns the number of occurrences of that string in the string on which we performed the operation.

This method is useful when, for example, we want to check if a certain phrase is repeated more than once in a given string:

```python
>>> 'Ala has a cat'.count('has')
1
>>> 'Ala has a cat but Ola has a dog'.count('has')
2
```

:snake: Copy the content of one of the paragraphs on this page, use it to define a string and use the `count` method on it to check how many times the following character sequences appear in it: `i`, `string`, and `on`.


## String length, `len` function

One of the most useful operations we can perform on a string is to check its length. For example, we want to check if it is not too long, or we want to compare the length of two strings. Here, the `len` function comes in handy.

```python
>>> len('Winnie the Pooh')
15
```

Note that `len` is not a method, so we do not use the notation `object.method()`. This is because checking the length of an object (in this case: string) is such a popular operation in Python that a separate function was created to perform it.

:snake: Check the length of your first and last name. See what length an empty string, which is `''`, has.

## :pushpin: Summary

In this chapter:

* we have learned what a **string** is,
* we have learned the meaning of the words **method** and **argument**,
* we have learned the most important methods that can be called on a string,
* we have learned the `len` function, which returns the length of the string.

:checkered_flag: Next chapter: [`help` function](./03_help.md)
:checkered_flag:
