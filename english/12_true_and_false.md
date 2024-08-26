# Chapter 12. True and False

In this chapter:

* you will learn the concepts of "truth" and "false" and their representation in Python: `True` and `False`,
* you will learn the **conditional statement** `if`, which allows you to change the course of the program if a certain condition is met.


## True and False conditions

The programs we have written so far consisted of operations that Python
executed one after another. When one instruction was successfully
completed, the program moved on to the next one.
When writing more programs, you will quickly realize that this scenario
will not always suit you, because often we want certain operations to be
performed only when a certain condition is met.

For example, we have a list of numbers and we want to iterate through its elements, printing only the odd ones. In this case, the condition for printing the number on the screen is "the number is odd".

Programming languages allow us to define such conditions and check them. The result of such a check is **true** or **false**. True indicates a situation in which the condition has been fulfilled. The opposite is false. For example, the result of the condition "a giraffe is a bird" is false, while the result for "the Earth is not flat" is true.

Of course, in programs, such abstract conditions are not created. Instead, we will compare variable values, check if the result of a function has a specific value, etc. In this chapter, you will learn how to perform such operations and how to write programs that execute different instructions depending on whether a certain condition has been met.


## Conditions in Python, `True` and `False`

In Python, we have a range of operators at our disposal that allow us to check the truthfulness of expressions. We can, for example, compare values. The operator `==` is used for this purpose.

```python
>>> 1 == 2
False
>>> (2 + 2) == (2 * 2)
True
```

The opposite of the `==` operator is `!=`.

```python
>>> 'ala' != 'Ala'
True
>>> [1, 2] != [1, 2]
False
```

We can also check if one value is greater or less than the other:

```python
>>> 100 > 70
True
>>> 70 > 100
False
```

The operators `>` and `<` can be combined with `=`, creating the conditions "greater than or equal to" and "less than or equal to".

```python
>>> 3 >= 2
True
>>> 2 >= 2
True
>>> 1 >= 2
False
```

Note that in one expression, multiple operators can be used.

```python
>>> 1 <= 2 < 3 <= 3 < 4
True
```

Furthermore, we can negate the entire expression by writing `not` at the beginning.

```python
>>> not 1 == 1
False
>>> not 1 == 2
True
```

Of course, in each case, we can replace the values entered directly with variables and preserve the result of the expression.

```python
>>> temperature = 26
>>> is_cold = temperature < 10
>>> print(is_cold)
False
```


## Comparing strings

Comparing numbers seems understandable, but how are strings compared? The answer is simpler than it may seem: alphabetically. Letters that come later in the alphabet are considered "greater" than those that come earlier. Additionally, lowercase letters are considered "greater" than uppercase letters.

```python
>>> 'A' < 'B' < 'a' < 'b'
True
```

What about strings that have more than one character? They are compared
character by character until one of them is different, or until one of
the strings is longer. In the latter case, the string with more characters will be greater.

```python
>>> 'a' < 'ala'
True
>>> 'ala' == 'ala'
True
>>> 'ala' < 'ala ma kota'
True
```


## `in` operator

In addition to the operators discussed so far, there is one more that is useful, especially when working with lists. The `in` operator returns `True` if a given element is present in the list.

```python
>>> 'Basia' in ['Tomek', 'Magda', 'Karol', 'Basia']
True
>>> 12 in [10, 20, 30, 40]
False
```

## `if` statement

Checking if an expression is true would not make much sense if we couldn't use it to make decisions about the further course of our program. For this purpose, we use the **conditional statement** `if`:

```python
if temperature > 30.0:
    print('It is so so hot!')
```

The structure of this instruction is very simple: after the word `if`, we enter
a condition, then a colon and in the following lines, indented, instructions
that will be executed if the condition is true (we say: if the condition is
fulfilled).

:snake: Write a function that takes arguments `element` and `list` and if the given element is on the list, returns its position (use the `index` method), otherwise returns `-1`.

:snake: Write a function `quotient` that takes arguments `dividend` and `divisor`. If the divisor is not equal to zero, the function should return the result of division. Otherwise, it should print an error message.

## `if ... else` and `elif`

We can add a second part to the `if` statement that will be executed only if the condition is not fulfilled.

```python
if hour <= departure_time:
    print('Departure time:', departure_time)
else:
    print('We apologize for the delay')
```

Pay attention to the indentation in the code: `if` and `else` are on the same level.

If we want, we can check several alternative conditions within one `if` statement, if the previous ones turn out to be false.

```python
if 5 <= godzina < 12:
    print('morning')
elif godzina == 12:
    print('noon')
elif 12 < godzina < 17:
    print('afternoon')
elif 17 < godzina < 20:
    print('evening')
else:
    print('night')
```

:snake: Write a function that compares two numbers. As arguments, it should take numbers `a` and `b`. If `a` is greater than `b`, it should return 1, if the numbers are equal `0`, and if `a` is less than `b`, `-1`. Additionally, depending on the comparison result, the function should print one of the following messages: `a < b`, `a == b` or `a > b`.


## Combining conditions

Sometimes we will want to perform certain operations only if several conditions are met at the same time. In this case, we can use the `and` operator.

```python
if substance == 'water' and temperature > 100:
    state = 'water vapor'
```

If we wanted the operation to be performed if at least one of several conditions is met, we should use the `or` operator.

```python
if product == 'juice' or product == 'tea':
    cena = 4.50
```

Operators `or` and `and` can be combined in one expression.


## Object truthfulness, the `bool` function.

The condition does not have to be a comparison. Each type of object defines truth in some way. For example, an empty list is false, while a list with at least one element is true.

To determine the value of a given object in terms of logic, we can use the built-in function `bool`. It takes one argument - any object - and returns its logical value: `True` or `False`.

```python
>>> bool([])
False
>>> bool([1, 2, 3])
True
```

:snake: For each of the following types, find a value for which the `bool` function will return `True` and one for which it will return `False`: string, tuple, integer, float.

Since every object can be considered in terms of "truthfulness", we can use any object in an `if` statement.

```python
if name and surname and len(password) > 5:
    print('Correct data provided')
```

:snake: Write a function that takes a list as an argument and returns `True` if all elements in this list are true, or `False` if at least one element is not true.

## :pushpin: Summary

In this chapter:

* we have learned how to check the truthfulness of expressions,
* we have learned the `if` statement, which can change the course of the program when a specified expression is true.

---

:checkered_flag: Next chapter: [Dictionaries](./13_dictionaries.md) :checkered_flag:
