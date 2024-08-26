# Chapter 5. Errors

In this chapter:

* you will learn what **exceptions** are,
* how to read error messages.

## Exceptions

When creating programs, we are never able to predict all the situations that may occur. Sometimes the user will provide data that our program is unable to process: for example, we expected a number but received text instead. Other times, we may make a mistake and call a method on an object that does not exist. In each of these situations, Python will respond by reporting an error.

When this happens, the program will be interrupted and a message will be displayed, which will allow us to find out what our mistake was, which will allow us to correct the code of the program to avoid the same problem in the future.

The words "error" or "problem" are very general, because they can also apply to things that as programmers we have no control over. That is why we use the term **exception**, which only refers to those cases that the programming language can handle - meaning those that our programs can react to.

In practice, an exception is a situation in which Python has stopped executing the program because it encountered an *exceptional* situation that it was unable to handle on its own. It is said that the program **threw an exception**. When this happens, it is the role of the programmer to adjust the program in such a way that a similar situation does not result in a stop in the future.

What are the unique situations we mentioned? It could be an attempt to perform an operation that Python is unable to execute, such as adding a number to text. Or an error of "not enough space on the hard drive" while saving a file. It is impossible to list all such possibilities - over time you will become familiar with the most common exceptions and learn to anticipate which operations may have caused them.

## How to read error messages and exceptions

Let's try to trigger an error and see how our program behaves.
Do you remember how we mentioned that we insert strings in single or double quotes, but you have to make sure that the closing quote is the same as the opening one? Let's do an experiment and see what happens when we break this rule.

```python
>>> 'ala ma kota"
Traceback (most recent call last):
  File "python", line 1
    'ala ma kota"
                ^
SyntaxError: EOL while scanning string literal
```

As you can see, instead of displaying this phrase, Python reported an error.
Let's read it line by line.

* At the very beginning, we always see the message `Traceback (most recent call last):`. The word "traceback" refers to a list of operations that caused an error. In this case, only one operation was performed (returning the entered phrase), but in the future, you may encounter situations where an exception or error was thrown as a result of executing a whole sequence of commands. Python always shows the entire traceback so that the programmer can understand what went wrong. The text `most recent call last` indicates that the last operation on the list was executed most recently compared to all the others.

* `File "python", line 1` is the traceback. In our case, it is only one line. Here we see a description of the place where the error occurred.

* The last line contains the most important information, which is the direct cause of the error. It starts with the type of exception. In this case, it is `SyntaxError` - a syntax error. The type of error can be understood as a category: it does not tell us exactly what the error was, but it allows us to classify different exceptions to make them easier to understand. `SyntaxError` means an error in the syntax of the string of characters, which should follow each other according to the language syntax. Let's decipher the abbreviation EOL - end of line. After such a message, we know a little more about which part of our code to look at. Discovering the reason can be not easy.

When creating more advanced programs, you will encounter even longer error messages. Don't let this discourage you: every exception comes down to just one incorrect operation, and a traceback, no matter how long, will help you locate the cause of the failure. If you still cannot understand why your program stopped working, paste the last line of the message into a search engine. It is very likely that someone has already encountered the same problem and found a solution.

Exceptions are often a way for the program you're writing to communicate with the user running it. They help inform the user about what went wrong. Below, we can see how the error message for the same issue has changed between Python versions.

In version 3.7, Python returned the error `SyntaxError: EOL while scanning string literal`, and without knowing what "EOL" means in programming jargon, it would be difficult to understand what the problem is with the provided string.

In version 3.12, Python returns the error `SyntaxError: unterminated string literal (detected at line 1)`, which is more understandable because it directly informs us that the provided string is simply not closed.

```python
# Python version 3.7
>>> 'ala ma kota"
Traceback (most recent call last):
  File "python", line 1
    'ala ma kota"
                ^
SyntaxError: EOL while scanning string literal

# Python version 3.12
>>> 'ala ma kota"
  File "python", line 1
    'ala ma kota"
    ^
SyntaxError: unterminated string literal (detected at line 1)
```

:snake: Invoke errors and read exceptions caused by the following operations: division by zero; calling the lower() method on any digit; calling a method on any string that does not exist; executing code that does not make sense (you can enter a random string of characters).

## :pushpin: Summary

In this chapter:

* we have learned what an **exception** is and how to read its content.

---

:checkered_flag: Next chapter: [Variables](./06_variables.md) :checkered_flag:
