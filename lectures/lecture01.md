<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #1
Monday May 9, 2022

## Lecture Objective

- this lecture aims to provide an overview of the language and provide the student an opportunity to practice working with Python's interactive mode

## Pre-requisites

- This semester (Summer 2022) we will be using Python version 3.9.9
    - To check the version of Python installed on your system: `python3 -V`.
- Prior programming experience and use of Raspberry Pi

## Page Contents
- [Variable declarations](#variable-declarations)
- [Python conventions](#python-conventions)
- [Python data types (Numbers and Strings)](#python-data-types-(numbers-and-strings))
- [Python operators (arithmetic)](#python-operators-(arithmetic))
- [Python operators (relational)](#python-operators-(relational))
- [Python Logical operators](#python-logical-operators)
- [Python Bitwise operators](#python-bitwise-operators)
- [Python Assignment (compound) operators](#python-assignment-(compound)-operators)
- [Python Special operators](#python-special-operators)
- [Accepting standard (user) input in Python](#accepting-standard-(user)-input-in-python)
- [Python decision control](#python-decision-control)
- [Python loops](#python-loops)
- [Python inline for loop](#python-inline-for-loop)
- [Python Strings](#python-strings)
- [Python environment variables](#python-environment-variables)
- [Class Exercise A](#class-exercise-a)
- [Class Exercise B](#class-exercise-b)
- [Class Exercise C](#class-exercise-c)

----------------------------------

## Variable declarations
All variable names in Python must adhere to the following rules:
1. Must begin with either an alphabetic [A-Za-z] or underscore _ character.
2. After the first character, may consist of any number of alphabetic
   [A-Za-z], numeric [0-9] and underscore _ characters.
3. Variable names may NOT contain any special or punctuation characters
   (eg. *, /, ., #, $, %, etc.).
4. Variable names may not be the same as a Python language reserved keywords,
   functions, and miscellaneous identifiers.
   Please refer to <a href="../pythonKeywords.html" target="_blank">pythonKeywords</a> for a complete list.
5. The Python programming language is case sensitive, so the identifiers
   'apple', 'Apple', and 'APPLE' are all considered to be unique and
   distinct variables.

## Python conventions
1. Please adhere to the [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) 
    when coding and declaring variable names
   (i.e. `total_price`, `speed_of_light`, `dna_sequence_main`, `image_rotation`, etc.)

   In the majority of cases, use `snake_case` rather than `camelCase` naming convention

   See [here for naming styles](https://realpython.com/python-pep8/#naming-styles) and [here for guidelines in choosing variable names](https://realpython.com/python-pep8/#naming-styles)

 2. In Python, code blocks are defined by their [indentation](https://peps.python.org/pep-0008/#indentation).
    A "code block" encompasses functions, if statements, for loops,
    while loops, etc. Indenting starts a block and unindenting ends it.
    There are no explicit braces, brackets, or keywords. This means
    that whitespace is significant, and MUST BE consistent. 
    Therefore, blocks of should be consistently indented by the same
    amount of whitespace (minimum of 3 spaces and maximum of 4 spaces).
    Uses of tabs are permitted, but your text editor should be instructed
    to convert TABS to SPACES (to allow for consistency when
    usubmitting your code).


## Python data types (Numbers and Strings)
### Numbers

Numbers consist of mainly of two types - integers and floats.
- Examples of integers are 2, 8, -13 which are simply whole numbers.
- Examples of floating point numbers (or floats for short) are 3.14
and 87.3E-4 . The E notation here indicates powers of 10. In this case,
87.3E-4 means 87.3 * 10 ** -4 (where ** indicates an exponent)

### Strings
Strings can be specified as either single or double quoted. Strings
declared using single or double quotes such as 'Beware of the dark side'
preserve all white space (i.e. spaces and tabs within the quotes are
preserved as-is.)

Python also allows for multi-line strings using triple quotes ( `"""` or `'''` ).
Triple quoted strings allow the use of single and double quotes freely
within the triple quotes. An example is:
```
myString = """This is a multi-line string. This is the first line.
This is the second line.
'Who are you?,'
'Bond, James Bond.'
"""
```
OR
```
myString = '''This is a multi-line string. This is the first line.
This is the second line.
"Who are you?,"
"Bond, James Bond."
'''
```

Strings however are immutable meaning that once they have been created,
strings cannot be changed.


## Python operators (arithmetic)
|    |              |
|----|:-------------|
|+   | Add two operands or unary plus |
|-   | Subtract right operand from the left or unary minus |
|*   | Multiply two operands |
|/   | Divide left operand by the right one (always results in float) |
|%   | Modulus - remainder of the division of left operand by the right |
|//  | Floor division - division that results in whole number adjusted to the left in the number line|
|**  | Exponent - left operand raised to the power of right |

```
x = 15
y = 4
```
```
print('x + y = ', x + y) # Output: x + y = 19
```
```
print('x - y = ', x - y) # Output: x - y = 11
```
```
print('x * y = ', x * y) # Output: x * y = 60
```
```
print('x / y = ', x / y) # Output: x / y = 3.75
```
```
print('x // y = ', x // y) # Output: x // y = 3
```
```
print('x ** y = ', x ** y) # Output: x ** y = 50625
```

As in mathematics, parentheses `( )` can be used to alter the order
of operations in a Python program.

```
n3 = 8
print(3 + 7 * n3, "\n") # answer here is 59 (order of operations in effect BEDMAS)
```
```
print("2 to the exponent 5 is: ", 2**5, "\n") # 32
```
```
print("-2 to a positive exponent like 6 is: ", -2**6, "\n")
```
The answer above should be +64, but it is instead -64!
Again, operator precedence is a factor here, the ** exponent
is evaluated first!

To correct the problem, the -neg value must be placed in (-2)
```
print("-2 to a positive exponent like 6 is: ", (-2)**6, "\n")
```
```
print("3 divided by 4 is: ", 3/4, " but 3 modulo 4 is: ", 3%4, "\n")
```

## Python operators (relational)
Relational operators are used to compare values, returning either
`True` or `False` according to the condition.
|    |                                  |
|----|----------------------------------|
| &gt; |  Greater than |
| &lt; |  Less than |
| == | Equal to |
| != | Not equal to |
| &gt;= | Greater than or equal to |
| &lt;= | Less than or equal to |
```
print("Is 5 == 5? ", 5 == 5, "\n")
```
```
print("Is 3 < 4? ", 3 < 4, "\n")
```
```
print("Is 6 < 6 ? ", 6 < 6, "\n")
```
```
print("Is 7 != 5? ", 7 != 5, "\n")
```
```
print("Is 9 > 4 ? ", 9 > 4, "\n")
```
```
print("Is 6 >= 6? ", 6 >= 6, "\n")
```

## Python Logical operators
In Python, Logical operators are specified with `and`, `or`, and `not`.

|    |                                  |
|----|----------------------------------|
|and | True if both the operands are true |
|or  | True if either of the operands is true |
|not | True if operand is false |

```
x1 = True
y1 = False
```
```
print('x1 and y1 is ', x1 and y1) # Output: x1 and y1 is False
```
```
print('x1 or y1 is ', x1 or y1) # Output: x1 or y1 is True
```
```
print('not x1 is ', not x1) # Output: not x1 is False
```

## Python Bitwise operators
Bitwise operators act on operands as if they were strings of binary
digits (i.e. they operate on a bit by bit basis).

For example, the value 10 in binary is `0000 1010` and 4 is `0000 0100`

|    |                |                  |
|----|----------------|:------------------|
| &amp; |  Bitwise AND | `x & y = 0 (0000 0000)` |
| \| |  Bitwise OR | `x | y = 14 (0000 1110)` |
| ~  | Bitwise NOT | `~x = -11 (1111 0101)` |
| ^  | Bitwise XOR | `x ^ y = 14 (0000 1110)` |
| &gt;&gt; | Bitwise right shift | `x >> 2 = 2 (0000 0010)` |
| &lt;&lt; | Bitwise left shift | `x << 2 = 40 (0010 1000)` |


## Python Assignment (compound) operators
Assignment operators are used in Python to assign values to variables.

|    |                |
|----|----------------|
| =  | x = 5 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 5 |
| /= | x /= 5 |
| %= | x %= 5 |
| //= |  x //= 5 |
| **=  | x **= 5 |
| &amp;= |  x &amp;= 5 |
| \|= | x \|= 5 |
| ^= | x ^= 5 |
| &gt;&gt;= |  x &gt;&gt;= 5 |
| &lt;&lt;= |  x &lt;&lt;= 5 |


## Python Special operators
The Python programming language offers some special type of operators
like the identity operator or the membership operator. 

The operators `is` and `is not` are the identity operators in Python.
They are used to check if two values (or variables) are located in the
same part of the memory. Two variables that are equal does not imply that
they are identical.
|    |                |
|----|----------------|
| is     | True if the operands are identical (refer to same object) |
| is not | True if the operands are not identical (do not refer to same object) |

```
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3] # a list (array)
y3 = [1, 2, 3]
```
```
# Output: False
print(x1 is not y1)
print(id(x1), id(y1))
```
```
# Output: True
print(x2 is y2)
print(x1 is y1)
print(id(x2), id(y2))
```
```
# Output: False
print(x3 is y3)
print(id(x3), id(y3))
```
```
# Output: False
x4 = x3
print(x4 is x3)
print(id(x4), id(x3))
```
The last example above demonstrates python variable referencing.  A good explanation between differences between Python and C/C++ are here:
- [Understanding Python variables and Memory Management](http://foobarnbaz.com/2012/07/08/understanding-python-variables/)
- [Is Python pass-by-reference or pass-by-value?](https://robertheaton.com/2014/02/09/pythons-pass-by-object-reference-as-explained-by-philip-k-dick/)



In Python, the `id( )` built-in function returns the "identity"
of an object. This is an integer which is guaranteed to be unique
and constant for this object during its lifetime.

For a complete list of Python built-in functions, please refer to:
<a href="https://docs.python.org/3/library/functions.html" target="_blank">https://docs.python.org/3/library/functions.html</a>

## Accepting standard (user) input in Python
```
population = input("Population of Toronto is? ")
```
```
print(population, type(population))
```

With one argument, the `type( )` built-in function returns the type of
an object. The return value is a type object and generally the same
object as returned by `object.__class__`
```
print(population.__class__)
```

## Python decision control
Making decisions in programs are used when requiring the execution
of code only if a certain condition is satisfied.
To achieve this in Python, the `if`/ `elif` / `else` control structure
is used.

Python `if` statement syntax:
```
if test expression :
   statement(s)
```

The program evaluates the test expression and executes the
statement(s) only if the test expression is `True`.
If the test expression is `False`, the statement(s) is not executed.

In Python, the body of the `if` statement is indicated by indentation
and is a requirement in ALL logical control structures.
The body of the control structure starts with an indentation and ends
with the first unindented line.
With respect to the test expression, Python interprets ALL non-zero
values as `True`, with the expressions `None` and `0` interpreted as `False`.

Example:

If the number is positive, we print an appropriate message
```
xValue = 3
yValue = -2
if xValue >= 0 :
   print(xValue, "is a positive number!")
print("This is always printed.")

if yValue >= 0 :
    print(yValue, "is a positive number!")
else :
    print(yValue, "is a negative number!")

print("This is also always printed.")
```
<img src="images/if_elif_else_statement.jpg" width="412" height="407" />

```
if xValue >= 0 :
   print(xValue, "is a positive number!")
elif yValue >= 0 :
    print(yValue, "is a positive number!")
else :
    print("both", xValue, "and", yValue, "are negative numbers!")
# end if
```

Example using logical operators and / or
```
if xValue >= 0 and yValue &gt;= 0 :
    print("both", xValue, "and", yValue, "are positive numbers!")
elif xValue >= 0 :
   print(xValue, "is a positive number!")
elif yValue >= 0 :
   print(yValue, "is a positive number!")
else :
   print("both", xValue, "and", yValue, "are negative numbers!")
```
Example using logical operators and / or and nested controls
```
year = int(input("enter a whole number year: "))
```
NOTE: The `int( )` function is used to wrap the `input( )` function in order
to convert the string input to an integer
```
if year % 400 == 0 :
   print(year, "is a leap year!")
else :
   if year % 4 == 0 and year % 100 != 0 :
      print(year, "is a leap year!")
   else :
      print(year, "is NOT a leap year!")
   # end if
# end if
```

alternate example of logic above (refer to [Python 3 operator precedence reference](https://docs.python.org/3/reference/expressions.html#operator-precedence))
```
year = int(input("enter a whole number year: "))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
   print(year, "is a leap year!")
else :
   print(year, "is NOT a leap year!")
# end if
```

## Python loops
The `for` loop in Python is used to iterate over a sequence
(list, tuple, string) or other iterable objects. Iterating over
a sequence is called  a traversal.
Syntax of the `for` Loop
```
for item in sequence:
   body of for loop
   statement(s)
```

Here, item is the variable that takes the value of each iteration
within sequence.
The loop continues until the last item in the sequence is evaluated.
The body of the for loop is separated from the rest of the code
using indentation.

The `range( )` function:
To generate a sequence of numbers, the `range( )` function can be used.
- For example, `range(10)` will generate numbers from 0 to 9 (10 numbers).
- The `range( )` function can also specify the start, stop and step size with:
`range(start, stop, step)` step defaults to 1 if not provided.
- The `range( )` function does not store all the values in memory,
- Instead, `range( )` remembers the start, stop, and step and generates
the next number at runtime.

Examples:
```
for i in range(0, 9) :
   print(i, end="") # the end="" is used to suppress newlines
print( )

for i in range(0, 9, 2) : # step by 2 (i.e. 0, 2, 4, 6, 8)
   print(i, end="")
print( )
```
```
for i in range(ord('a'), ord('z') + 1) :
   print(chr(i), end="")
# end
print( )
```

## Python inline for loop
```
print('|'.join(("%s" % x) for x in range(1, 5)))
```

In Python, a `for` loop can have an optional `else` block as well.
The `else` portion is executed when the items in the sequence used to
iterate through the for loop is exhausted.

Example:
```
for i in range(1, 10):
   print(i, " ", end="")
else:
   print("No more items to process...")
print( )
```

As with other programming languages, the `break` statement can be used
to stop a `for` loop. In such case, the `else` portion is ignored.
Therefore a `for` loop's `else` portion will always execute as long
as no `break` is encountered.

Example:
```
for i in range(1, 10):
   if i == 5 :
      break
   print(i, " ", end="")
else:
   print("No more items to process...")
print( )
```

The `while` loop in Python is used to iterate over a block of code
as long as the test expression (condition) is true.

As with other programming languages, `while` loops are generally used
when the end or terminating condition is not known beforehand.
Syntax of `while` loop in Python:
```
while <test expression>:
   body of while loop
   statement(s)
```
With the `while` loop, the test expression is checked first. The body
of the loop is entered only if the test expression evaluates to `True`.
After one iteration, the test expression is checked again. This process
continues until the test expression evaluates to `False`.

As with the `for` loop, in Python, the body of the `while` loop is
determined through indentation.
The body starts with indentation and the first unindented line marks
the end of the loop.
One again, Python interprets any non-zero value as `True`, and `None` and `0` are
interpreted as `False`.

Examples:

Program to compute the sum of consequtive natural numbers from 1 to n
`sum = 1 + 2 + 3 + ... + n`
```
n = int(input("Enter a whole number > 0: "))
```
initialize `sum` and counter
```
sum = 0
i = 1
while i <= n:
   sum = sum + i
   i = i + 1    # update counter
# end of while loop
```
```
print("the sum of the numbers from 1 to", n, "is:", sum)
```

As with the `for` loop, the `while` loop, can have an optional `else`
block.
The `else` block is executed when the condition in the `while` loop
evaluates to `False`. The `while` loop can also be terminated with the
`break` statement.
In such case, the `else` block is ignored.

Example:
```
counter = 0

while counter < 20:
   print("Inside loop counter is:", counter)
   counter = counter + 1
else:
   print("while loop terminated...")
```

## Python Strings
String function examples:
```
import string
lcLetters =  string.ascii_lowercase
ucLetters =  string.ascii_uppercase
digits = string.digits

str = "Apple INC."
print("original string:", str, "swapcase( ):", str.swapcase( ))
print("original string:", str, "title( ):", str.title( ))
print("original string:", str, "upper( ):", str.upper( ))
print("original string:", str, "lower( ):", str.lower( ))
print("original string:", str, "join(['1', '2', '3']):", str.join(['1', '2', '3']))
print("original string:", str, "reversed( ):", "".join(reversed(str)))
print("original str:", str)
```

## Python environment variables
Python environment variables can be accessed by importing the `os`
module and accessing the 'environ' dictionary key/value pairs.
To print all system environment variables:
```
import os
for key in os.environ :
   print("%-35s %s" % (key, os.environ[key]))
```

## Class Exercise A

Write the code for a Python program to display all of the
prime numbers within a lower and upper range (eg. 1000 to 2000).
Ask the user to enter the lower and upper ranges.
(eg.)
```
lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
```

HINT: Use a `for` loop with an iterator called 'x' that runs from
`lower` to `upper` inclusive.
Then, within the `for` loop, test to make sure the iterator 'x'
is > 1 and if it is, within that condition, execute another
`for` loop (with an iterator of 'y') that runs from 2 to 'x'.
Within the inner `for` loop, test to see if 'x' % 'y' == 0 and
if it is, simply `break` out of the loop.
Use an else block within the inner for loop that simply
prints 'x'.
```
#!/home/pi/software/bin/python3

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers from", lower, "to", upper, "are: ")
# your solution here...
```

## Class Exercise B
Write the code for a Python program that determines how many numbers
from 10 to 999 inclusive are Armstrong numbers!
A number is an Armstrong number if it is equal to the sum of
its own digits raised to the power of the number of digits it
contains.
So, for example, the number 153 is an Armstrong number because
1^3 + 5^3 + 3^3 = 153

HINT: There are exactly 4 Armstrong numbers from 10 to 999.

## Class Exercise C

Write the code for a Python program that asks the user to enter a
number from 0 to 10 inclusive. Any other value generates an error
message and then quits. Once the value is accepted, your program
draws a number pyramid with the first row starting at 0. Each
subsequent row contains 2 more numbers than the previous row such
that the middle number in each row increases by 1. Also, each row
begins with 0 and increases by 1 for each column until the middle
number is reached at which point, the numbers decrease until they
end with 0.

Also, each row displays spaces so that the pyramid appears as an
isoscelles triangle. The first row will contain row - 1 spaces, the
second row will contain row -  2 spaces, etc.

For example, a 3 row pyramid looks like:
```
  0
 010
01210
```

For example, a 10 row pyramid looks like:
```
    	 0
    	010
       01210
      0123210
     012343210
    01234543210
   0123456543210
  012345676543210
 01234567876543210
0123456789876543210
```