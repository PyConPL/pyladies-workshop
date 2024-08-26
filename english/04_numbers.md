# Chapter 4. Numbers

In this chapter:

* you will learn what `integer` and `float` are,
* you will learn how to perform arithmetic operations on numbers.

## Integers

To define an integer, simply type it without putting spaces between the digits:

```python
>>> 2024
2024
```

We can add and subtract numbers:

```python
>>> 20 + 17
37
>>> 2 + 0 + 1 + 7
10
>>> 20 - 17
3
>>> 20 - 1 - 7
12
```

...multiply and divide:

```python
>>> 20 * 17
340
>>> 20 / 17
1.1764705882352942
```

...divide completely:

```python
>>> 20 // 17
1
```

...raising to the power:

```python
>>> 201 ** 7
13254776280841401
```

...or to check the remainder of division (modulo):

```python
>>> 20 % 17
3
```

We can combine all of these operations in any way we want.

```python
>>> 20 / 2 + 17 * 3
61
```

If we want to have more control over the order of operations, we can use parentheses:

```python
>>> (20 * (2 + 17)) / 3
126
```

:snake: Calculate the following values: 

* the sum of today's day, month number, and year,
*t he result of dividing the year of your birth by the sum of the day and month on which you were born.


## Real numbers

All of the above operations can also be performed on real numbers (**float**, floating-point):

```python
>>> 2.5 * 2.0
5.0
>>> 7 / 2.0
3.5
>>> 6.7 + 0.3 - 2.5
4.5
>>> 1.0 / 3
0.3333333333333333
```

:snake: Do you know when Python will return a *float* and when an *integer*? Make sure to check different combinations of numbers and operations.


## Operators and their order

The symbols we use to perform operations (`+`, `*`, etc.) are called **operators**.
Each operator has its own priority, which means that if multiple different operators are used in one operation (e.g. `2 + 1 * 3`), Python will first calculate those with a higher priority.

For example, in such an operation:

```python
>>> 4 + 10 * 6
```

First, multiplication will be performed and only then addition, because the `*` operator has a higher priority than `+`, which means the result will be `64`.

The table below presents operators and their meanings. The order of rows corresponds to priority, meaning that operators with the highest priority are at the top and those with the lowest are at the bottom.

Operators | Meaning
--------- | ---------
`**` | Exponentiation
`*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo
`+`, `-`  | Addition, subtraction

## :pushpin: Summary

In this chapter:

* we learned how to define **integers** and floating point numbers (**float**), and we also familiarized ourselves with the most important mathematical **operators** and their priorities.

---

:checkered_flag: Next chapter: [Errors](./05_errors.md) :checkered_flag:
