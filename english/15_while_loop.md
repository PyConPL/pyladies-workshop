# Chapter 15. `while` loop

In this chapter:

* you will learn how to use the `while` loop.


## The `while` loop

You already know what a loop is and you know one of them: `for`. Now you will learn the second, and at the same time the last one that exists in Python: `while`. Its structure is even simpler than the previous one:

```python
counter = 1
while counter < 10:
    print(counter)
    counter = counter + 1
```

We start the definition of a loop with the word `while`, then we define the condition (just like in the `if` statement), and after a colon, in subsequent lines and indented, we write the instructions that will be executed as long as the condition is true.

Note that if we define a condition that will always be true, then the loop will be executed infinitely.

```python
while 1 == 1:
    print('.')
```

:snake: Write a function that takes a list as an argument and prints all its elements using a `while` loop.

## :pushpin: Summary

In this chapter:

* we have learned the `while` loop.


---

:checkered_flag: Next chapter: [Standard library](./16_standard_library.md) :checkered_flag:
