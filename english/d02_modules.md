# Appendix 2. Modules

As mentioned in the chapter ["Standard Library"](./16_standard_library.md), anyone can create their own module (library) for Python and share it with others, or simply use it in different projects. Below you will read about how to create modules and how to use them.

## Writing a module

If you have [IDLE program](../d01_instalacja_pythona.md') on your computer, you probably already know that the code of programs written in Python is saved in files with the extension `.py`. This is a convention that allows for easy distinction between Python code and other files that do not contain it.

Every file with the extension `.py` is also a program that we can run in Python. In other words: if we run Python and open a file with the extension `.py`, the code contained in this file will be executed.

At the same time, every file with the extension `.py` is also a module. This means that we can import it in another file using the `import` statement and thus gain access to all the objects defined within it: functions, variables, etc.

In summary: to write a module, all you need to do is place any code in a file with the extension `.py`. Each such file can potentially be used as a module.

## Importing Modules

We can use the ready-made module in any other program or module by importing it there. It is important for both files to be located **in the same directory**, otherwise Python will throw an `ImportError` exception.

We import the module using the `import` statement, in which we provide its name, which is the same as the name of the file in which we saved it, but without the `.py` extension.

Let's assume that we have created a file named `functions.py` and saved the following code in it:

The following is a translation of the previous paragraph and the given Python code into English:

```python
def sum(a, b):
    return a + b
```

Now in the same directory, we can create a file `calculations.py` and enter the following code in it:

```python
import functions

print(functions.sum(2000, 17))
```

If we run the `calculations.py` program, the number `2017` will be printed on the screen.

## Usage of modules

Modules are one of the most powerful mechanisms in Python. They allow us to divide programs into logically separated fragments. For example, in one module we can place all the functions responsible for mathematical calculations, in another functions for displaying data on the screen, and in the third combine everything together using the other two modules.

When writing programs, always keep in mind that dividing them into modules increases the readability of your code. It will also be easier for you to return to a program whose code has been organized in such a way.
