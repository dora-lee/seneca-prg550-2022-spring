<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #4
Monday May 30, 2022

## Lecture Objective

- Gain understanding of Python file operations in order to demonstrate use when manipulating files
- Learn how to use context manager with file handling
- Demonstrate expertise with Python error handling


## Pre-requisites

- Python version 3.9.9 installed on your computer and on Raspberry Pi
    check Python version with `python -V`

## Page Contents

- [Python File I/O](#Python-File-IO)
    - [Python file access modes](#Python-file-access-modes)
    - [Reading data from and writing data to files in Python](#Reading-data-from-and-writing-data-to-files-in-Python)
    - [Common Python file methods](#Common-Python-file-methods)
- [File Context Manager](#File-Context-Manager)
- [Python Exception Handling](#Python-Exception-Handling)
    - [What is an Exception?](#What-is-an-Exception)
    - [Handling an exception](#Handling-an-exception)
    - [Standard Python exceptions](#Standard-Python-exceptions)
- [Class Exercises A](#Class-Exercises-A)
- [Class Exercises B](#Class-Exercises-B)
- [Class Exercises C](#Class-Exercises-C)


----------------------------------

## Python File I/O

A file is a named location on disk that stores information (often text data,
but may also consist of binary data).
Given that RAM is volatile memory (i.e. data stored in RAM is cleared
when the computer is turned off), files are used to permanently store
data in non-volatile memory (eg. hard disk).

The Python language has a built-in function `open()` that is used to open
a file on disk. This function returns a file object, also called a handle,
that can be used to read or write to the file as required.

Example:
```
fh1 = open("test.txt",'w')               # open file in current directory
fh2 = open("/home/pi/workspace/lectures/lecture04.txt",'w')  # open file using full path location (unix, linux)
fh3 = open("C:/Seneca/PRG550/lecture04.txt",'w')  # open file using full path location (windows)
```

Note the use of `/` to separate directories instead of `\` for Windows.  The forward-slash (`\`) is a special character and needs to be escaped if you want to include it in your string [Python Escape Characters](https://www.w3schools.com/python/gloss_python_escape_characters.asp).

```
fh4 = open("C:\\Seneca\\PRG550\\lecture04.txt",'w')  # full path with forward-slash escaped (windows)
```

When opening a file, the default access mode is for reading `r` in text
mode in which data is read into strings. However, the access mode can
be explicitly specified when opening a file (either for reading `r`,
writing `w` or appending `a`). It is also possible to specify that a file
be opened in text or binary mode.
When files are opened in binary mode, in place of reading data as strings,
data is read in bytes and is used when reading or writing non-text files
such as images or audio files.

### Python file access modes
| Mode|Description      |
|:----|:----------------|
| 'r' | Opens a file for reading. (default) |
| 'w' | Opens a file for writing. Creates a new file if it does not <br> already exist or overwrites the file if it does exist. |
| 'x' | Opens a file for exclusive creation, if the file already <br> exists the operation fails.|
| 'a' | Open a file for appending to the end of the file without overwriting <br> it, and creates a new file if it does not exist.|
| 't' | Opens the file in text mode. (default) |
| 'b' | Opens the file in binary mode. |
| '+' | Opens a file for updating (both reading and writing) |

A good illustration of mode characteristics given here [Python difference between `r+`, `w+` and `a+` in `open()`](https://mkyong.com/python/python-difference-between-r-w-and-a-in-open)

Examples:
```
fh1 = open("sample.txt")        # mode equivalent to 'r' or 'rt'
fh2 = open("sample.txt", 'w')   # open file to write in text mode
fh3 = open("image.png", 'r+b')  # open file read and write in binary mode
```

NOTE: Given that the default encoding will vary from platform to platform,
      it is highly recommended to specify the encoding type (`utf-8` used here [^1]) when opening
      a file.
```
fh4 = open("textFile.txt", mode='r', encoding='utf-8')
```
[^1]: [UTF08 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)

After file operations have been completed, the `close()` method is used
to properly close the file and free up system resources that were tied up
during file access.
Even though Python has a garbage collector to clean up unreferenced
objects, it is preferable to explicitly `close()` a file so that other
programs or system resources can access the file while the program is
running.
```
fh1 = open("sample.txt", encoding = 'utf-8')
fh1.close() # close the file
```

Visualization of Python file modes[^2]

<img src="images/python-file-modes.png" alt="python-file-modes" width="800" />

[^2]: [Stack Overflow](https://stackoverflow.com/a/30566011)

### Reading data from and writing data to files in Python

In order to write data to a file in Python, the file must be opened
for writing using mode `w` or appending `a` or using the exclusive
creation `x`.  Then, writing a string or sequence of bytes (for binary files) is performed
using the `write()` method. This method returns the number of characters
written to the file.

Example:
```
fh = open("test.txt", 'w', encoding = 'utf-8')
fh.write("first line in file\n")
fh.write("line #2\n")
fh.write("file line # three\n")
fh.close()
```

The program above will create (or overwrite if it does not exist) a file named
`test.txt` and writes three lines of data to the file.

NOTE: The newline character `\n` must be included to write data to a new line.

To read data from a file in Python, the file must be opened in read mode
and the `read(size)` method may be used to read in `size` number of bytes of data.
If `size` parameter is not specified, the method reads and returns contents up to
the end of the file.

For example, given the file `test.txt` created above, the following code:
```
fh = open("test.txt", 'r', encoding = 'utf-8')
data = fh.read(5)    # reads the first 5 bytes into data
print(data)          # displays 'first'

data = fh.read(5)    # reads the next 5 bytes into data
print(data)          # displays ' line'

data = fh.read()     # read in the rest of the file into data
print(data)          # displays:
                     # ' in file\nline #2\nfile line # three\n'
```
Once the end of file is reached, further calls to `read()` result
in empty strings.

In order to change the current file position (cursor) ahead of the next operation, the `seek()` method may be used. Similarly, the `tell()` method returns the current position (in number of bytes).

For example:
```
fh = open("test.txt", 'r') # open file for read (text mode)
data1 = fh.read(5)   # reads 5 bytes into data
print(fh.tell())     # displays the current file position: 5

fh.seek(0)           # moves file cursor to initial position (start of file)
data2 = fh.read(5)   # reads 5 bytes into data

print("{0}\n{1}".format(data1, data2))
```

Another example: A `for` loop that reads a text file one line at a time can be coded as: <a name="for-loop-read-file-lines"></a>
```
fh = open("test.txt", 'r', encoding = 'utf-8')
for line in fh:
   print(line, end = '')

fh.close()
```

NOTE: The lines read in from the file include the newline characters `\n`.

Alternately, the `readline()` method can be used to read individual lines of
from a file. The `readline()` method reads each line (including the newline)
character.
```
fh = open("test.txt", 'r', encoding = 'utf-8')
line = fh.readline()
print(line)
```

In addition to `readline()`, Python contains a `readlines()` method that
returns a list of all remaining lines in the entire file.
```
fh = open("test.txt", 'r', encoding = 'utf-8')
lines = fh.readlines()
print(lines)
```

All file read methods return empty strings when end of file (EOF) is reached.
```
fh = open("test.txt", 'r', encoding = 'utf-8')
lines = fh.readlines()
print(lines)
line = fh.readline() # what happens here?
print(">{0}<".format(line), len(line))
```
### Common Python file methods
|    |                 |
|----|:----------------|
| close()  | Close an open file. No effect if file is already closed. |
| fileno() | Return an integer number (file descriptor) of the file. |
| flush()  | Flush the write buffer of the file stream. |
| read(n)  | Read at most `n` characters form the file. <br> Reads until end of file if it is negative or `None`.|
| readable()      | Returns `True` if the file stream can be read from. |
| readline(n=-1)  | Read and return one line from the file. Reads in at most <br> `n` bytes if specified. |
| readlines(n=-1) | Read and return a list of lines from the file. Reads in <br> at most `n` bytes/characters if specified. |
| seek(offset,whence) | Change the file position to offset bytes with reference to file beginning (`whence=0`), current position (`whence=1`), or  file end (`whence=2`), .  |
| seekable() | Returns True if the file stream supports random access. |
| tell()     | Returns the current file location. |
| writable() | Returns True if the file stream can be written to. |
| write(s) |  Write string s to the file and return the number of <br> characters written. |
| writelines(lines) | Write a list of lines to the file. |

Examples:
```
f = open('test_seek', 'r+b')
print(f.writable())
f.write(b'0123456789abcdef')
f.seek(5) # Go to the 6th byte in the file
print(f.read(1))
print("at location {0} in file".format(f.tell()))       # where are we ?
f.seek(-3, 2)  # Go to the 3rd byte before the end
print(f.read(1))
```

## File Context Manager

The `with` statement starts a Python context manager and helps to wrap file-processing code in a logic layer that ensures that the file will be closed (and if needed, have its output flushed to disk) automatically on exit

For example:
```
with open("test.txt", 'r') as my_file:
   for line in my_file:
      print(line, end = '')
```
Contrast with the [for loop example](#for-loop-read-file-lines) above


## Python Exception Handling

### What is an Exception?
An exception is an event which occurs during the execution of a program
that disrupts the normal flow of the program's instructions. In general,
when a Python script encounters a situation that it cannot cope with, it
raises an exception. An exception is a Python object that represents an
error. When a Python script raises an exception, it must either handle
the exception immediately otherwise it terminates and quits.

### Handling an exception
When writing Python code that may raise an exception, the program can
be written in a defensive manner by placing the suspicious/potentially
problematic code in a `try` block. After the `try` block, an `except`
block of code is written that handles the problem as elegantly as possible.
Exception handling syntax:
```
try:
   # suspicious/potentially problematic code...

except Exception1:
   # if Exception1 occurs this block is executed.

except Exception2:
   # if Exception2 occurs this block is executed.

except Exception3, Exception4, ..., ExceptionN:
   # if Exception3 to ExceptionN occurs this block is executed.

except:
   # all other exceptions not specified above are handled here

else:
   # if there is no exception then execute this block.

finally:
   # always execute this block 
```

There are some important considerations regarding the exception
handling example above.
- A single `try` statement may have multiple `except` statements
which is useful if the `try` block contains statements that may
throw different types of exceptions.
- It is also possible to provide a generic except clause, which
handles any exception.
- After the `except` clause(s), an `else` clause may be included.
The code in the `else` block executes if the code in the `try` block
does not raise an exception.
- The `finally` clause allows a block of code to run regardless whether there 
is an error or not

The example below opens a file, writes some content to the file
and displays a completion message if no exception is encountered.
```
try:
   fh = open("testfile.txt", "w")
   bytes = fh.write("This is a test file for exception handling!!")
except OSError:
   print("Error: Cannot open file for writing...")
else:
   print("Successfully wrote", bytes, "bytes of data to the file...")
   fh.close()
```

The example below attempts to open a file for reading and displays
a completion message if no exception is encountered.
```
try:
   fh = open("unknown.txt", "r")
   s = fh.readline()
except OSError:
   print("Error: Cannot open file for reading...")
else:
   print("Successfully read '", s, "' from the file...")
   fh.close()
```

It is also possible to use the same `except` statement to handle multiple exceptions.

Example:
```
try:
   # suspicious/potentially problematic code...

except(Exception1 [, Exception2 [, ExceptionN]]]) :
   # If there is any exception from the given exception list,
   # then execute this block.
else :
   # If there is no exception then execute this block.
```

### Some Standard Python exceptions

This table lists some exceptions that are commonly encountered.  See [Python Exceptions](https://docs.python.org/3.9/library/exceptions.html#exception-hierarchy) for a complete list.

| Exception | Description |
|:----------|:----------------|
| StopIteration       | Raised when the next() method of an iterator does not point to any object. |
| SystemExit          | Raised by the sys.exit() function. |
| ArithmeticError     | Base class for all errors that occur for numeric calculation. |
| OverflowError       | Raised when a calculation exceeds maximum limit for a numeric type. |
| FloatingPointError  | Raised when a floating point calculation fails. |
| ZeroDivisionError   | Raised when division or modulo by zero takes place for all numeric types. |
| AssertionError      | Raised in case of failure of the Assert statement. |
| AttributeError      | Raised in case of failure of attribute reference or assignment. |
| EOFError            | Raised when there is no input from either the raw_input() or input() function and the end of file is reached. |
| ImportError         | Raised when an import statement fails. |
| KeyboardInterrupt   | Raised when the user interrupts program execution, usually by pressing ctrl + c. |
| LookupError         | Base class for all lookup errors. |
| IndexError          | Raised when an index is not found in a sequence. |
| KeyError            | Raised when the specified key is not found in the dictionary. |
| NameError           | Raised when an identifier is not found in the local or global namespace. |
| UnboundLocalError   | Raised when trying to access a local variable in a function or method but no value has been assigned to it. |
| OSError             | Raised for operating system-related errors. |
| SyntaxError         | Raised when there is an error in Python syntax. |
| IndentationError    | Raised when indentation is not specified properly. |
| SystemError         | Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit. |
| SystemExit          | Raised when Python interpreter is quit by using the sys.exit() function. If not handled in the code, causes the interpreter to exit. |
| TypeError           | Raised when an operation or function is attempted that is invalid for the specified data type. |
| ValueError          | Raised when the built-in function for a data type has the valid type of arguments, but the arguments have invalid values specified. |
| RuntimeError        | Raised when a generated error does not fall into any category. |
| NotImplementedError | Raised when an abstract method that needs to be implemented in an inherited class is not actually implemented. |
| ImportWarning       | Raised for warning about probable mistakes in module imports. |
| BytesWarning        | Raised for warnings related to bytes and bytearray. |

### Python Exception Hierarcy

Some exceptions are related and are grouped into categories.  For example `LookupError` includes two sub-errors
`IndexError` and `KeyError`.  Your code could generically handle both errors the same way, or it could handle each error differently.

Example to generically handle `LookupError`:
```
try:
   ... do something that triggers exception
except LookupError:
   ... handle_it()
```

Example to specifically handle the two sub-types of Python's built-in `LookupError`:
```
try:
   ... do something that triggers exception
except IndexError:
   ... handle_index_error()
except KeyError:
   ... handle_key_error()   
```
Example
```
try:
   ... do something that triggers exception
except IndexError:
   ... handle_index_error()
except KeyError:
   ... handle_key_error()
```


The class hierarchy for built-in exceptions is [^3]

```
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```           


[^3]: [Official Python Docs - Exception hierarchy](https://docs.python.org/3.9/library/exceptions.html#exception-hierarchy)

### Example error handling while reading `quotes.dat`
```
socrates#wisdom begins in wonder
holmes#insanity is often the logic of an accurate mind overtaxed
einstein#peace cannot be kept by force; it can only be achieved by understanding
huxley#logical consequences are the scarecrows of fools and the beacons of wise men
gates#640K ought to be enough for anybody.
longfellow#Whom the Gods would destroy they first make mad!
```
Example:
```
file_name = "quotes.dat"
quotes = { }
try:
   fh = open(file_name, "r", encoding="utf-8")
   for line in fh.readlines() :
      (author, quote) = line.split('#')
      quotes[author] = quote
   print(quotes)
except OSError:
   print("Error: Cannot open file", file_name, "for reading...")
else:
   print("Successfully read from", file_name, "file...")
   fh.close()
```

The `OSError` above will catch all errors related to 


## Class Exercises A
Write a python program that finds the longest word in a file
and displays the word and its length on the screen.

For the purposes of this exercise, a word is considered to be
a series on non-blank, non-whitespace characters.

HINT: Read each line in the file into a string, strip away the newline,
      then split the line into words using the space ' ' as a
      delimiter (assume there are no tabs).

## Class Exercises B
Write a Python program to count the frequency of words in a file.
The program's output should print the words found (one word per line)
followed by the word's frequency.

For the purposes of this exercise, a word is considered to be
a series alphabetic characters (upper or lowercase) ONLY!

Create a plain text file named `journey.txt` using the following text:
```
Once there lived a village of creatures along the bottom of a
great crystal river. Each creature in its own manner clung
tightly to the twigs and rocks of the river bottom, for clinging
was their way of life, and resisting the current what each had
learned from birth. But one creature said at last, "I trust that
the current knows where it is going. I shall let go, and let it take
me where it will. Clinging, I shall die of boredom." The other
creatures laughed and said, "Fool! Let go, and that current you
worship will throw you tumbled and smashed across the rocks,
and you will die quicker than boredom!" But the one heeded
them not, and taking a breath did let go, and at once was
tumbled and smashed by the current across the rocks. Yet, in
time, as the creature refused to cling again, the current lifted
him free from the bottom, and he was bruised and hurt no
more. And the creatures downstream, to whom he was a
stranger, cried, "See a miracle! A creature like ourselves, yet he
flies! See the Messiah, come to save us all!" And the one carried
in the current said, "I am no more Messiah than you. The river
delight to lift us free, if only we dare let go. Our true work is this
voyage, this adventure. But they cried the more, "Saviour!" all
the while clinging to the rocks, making legends of a Saviour.

--Richard Bach--
```

HINT: As above, read each line in the file into a string, strip away
      the newline, then split the line into words using the space ' '
      as a delimiter (assume there are no tabs). 
      Then, consider using the `filter()` function to remove non-alphabetic
      characters from each word (example below).
```
      s = "copy'rig-ht"
      filterObj = filter(str.isalnum, s)
      newStr = ""
      for char in filterObj :
         newStr += char
      print(newStr)
```
Consider storing each word in a Python dictionary with the word
as the key and the word's frequency as its value.

## Class Exercises C

Write a Python function named `copy_file` that accepts 2 parameters:
`from` that represent the name of a source file to read from 
`to` that represents the name of a target file to write to
It should copy the entire contents of the source file into the target file.

```
def copy_file(from, to)
```

You must use exception handling to check all file I/O operations.
