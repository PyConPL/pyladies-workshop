# Appendix 4. File operations

Files are often the source of data in programs. If a file contains text, which are characters that can be displayed on the screen, we call it a **text file**. Such a file can be read in a text editor, for example in Notepad. There are also files whose contents we do not interpret as text, such as images. We call them **binary files**.

Both types of files can be read and written in Python, however, in this article we will focus on text files. Once you learn how to work with them, operations on binary files will no longer be a problem for you.

## File path

The most important attribute of a file is its **path**, which indicates where it is located in the directory structure and under what name. For example, if you log in as a user "Ala" in the Windows system and create a file "cat.txt" in the "My Documents" directory, the path of this file will most likely look like this: `C:\Users\Ala\Documents\cat.txt`.

In Python, we store paths in strings, for example:

```python
>>> file_path = 'C:\Users\Ala\Documents\cat.txt'
>>> print(file_path)
C:\Users\Ala\Documents\cat.txt
```

In the above example, we defined an **absolute path**, which precisely specifies the directory in which the file is located (`C:\Users\Ala\Documents`). If we refer to a file relative to the directory in which our program is located, we can define a **relative path**. For example, we can only provide the file name: `cat.txt`. In this case, Python will assume that we are looking for the file in the same directory as the program. We can also say that the file is located in the "higher" directory: `..\cat.txt`.

Regardless of the chosen method, in order to operate on a file, we will need its path.

## Reading a file

The built-in function `open` gives us access to the file by taking the path as an argument.

```python
>>> file = open(path)
```

Once we define a file, we can read its entire content by calling the `read` method.

```python
>>> data = file.read()
>>> print(data)
file contents
```

We can also iterate through a file, line by line.

```python
for line in file:
    print(line)
```

When we read the file, a second attempt to read will return an empty string. This happens because Python keeps track of the position where we finished reading the file and starts subsequent reads from that position. If this position is at the end of the file, a second attempt to read will return nothing. To read the file from the beginning again, we must call the `seek` method with an argument of `0`, which will reset the reading position to the very beginning.

```python
>>> file = open('cat.txt')
>>> file.read()
'ala has a cat'
>>> file.read()
''
>>> file.seek(0)
>>> file.read()
'ala has a cat'
>>> file.read()
''
```

## Writing to a file

When opening a file with the `open` function, we can decide whether we want to perform reading or writing on it. By default, Python assumes reading. If we want to explicitly specify the **mode** of working with the file, we must pass a second argument, which should be a string. If we choose `'r'` (*read*), we will only be able to read the file. If `'w'` (*write*) is chosen, only writing will be possible. There are more available modes, which you can read about in the [documentation for the `open` function](https://docs.python.org/3/library/functions.html#open).

After opening the file in write mode, we can enter text into the file using the `write` method.

```python
>>> file = open('cat.txt', 'w')
>>> file.write('ala ma kota')
```

If there was any text in the file before opening it, it will be **overwritten** after calling the `write` method. However, subsequent writes to the already open file will cause the text to be appended at the end.

```python
>>> path = 'cat.txt'
>>> open(path).read()
'at the beginning there was such a text'
>>> file = open(path, 'w')
>>> file.write('now we will overwrite')
>>> file.write(' that text')
>>> file.close()
>>> open(path).read()
'now we will overwrite that text'
```

Note that in the above example, after saving the text, we called the `close` method. This way we closed the file, preserving the data on the disk. If we did not do this, calling the `read` method would return the original content of the file. The `close` method should be used if we want to read the same file again after saving. Otherwise, Python will automatically close the file: it will do so when the function in which we opened the file ends, or when the program finishes its execution.

## New line character

When working with text files, we will come across the **new line character**, which is represented in Python as a string with the content `\n` (backslash and the letter "n"). It indicates the place where a line of text ends. The character itself is not special, it is just a character like `a` or `7`. However, it is commonly accepted that the new line character has a special meaning in order to allow text to be divided into separate lines. Therefore, it is treated differently than other characters, for example the `print` function will replace it with a new line. Importantly, this character is not directly related to files - it can be a part of any string.

```python
>>> s = 'first line\nsecond line'
>>> print(s)
first line
second line
```
