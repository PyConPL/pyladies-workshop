# Appendix 3. The `input` function.

When writing a program, we often expect that its user will provide us with some data: their name and surname, numerical parameters, or other values that will affect the program's execution. The simplest method of obtaining such data is by using the built-in `input` function, which, when called, pauses the program's execution, waits for the user to type something and press enter, and then returns the entered text as a string:

```python
print('Enter your age:')
age = input()
print('You are {}'.format(age))
```

In the above example, we display a message on the screen - a request to enter age - then we retrieve this value from the user and display it in the next message.

Remember that the value obtained in this way will always be a string. If you want to convert it to a number, you can use the built-in function [`int`](https://docs.python.org/3/library/functions.html#int).
