<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #3
Tuesday May 24, 2022 and Wednesday May 25, 2022

## Lecture Objective

- Learn how to declare and use Python functions and what types of arguments they utilize
- Gain understanding for Python anonymous functions and their applications
- Demonstrate functional programming concepts using Python

## Pre-requisites

- Python version 3.9.9 installed on your computer and on Raspberry Pi
    check Python version with `python -V`

## Page Contents
- [Python Functions](#Python-Functions)
    - [Function Arguments in Python](#Function-Arguments-in-Python)
    - [Default Arguments](#Default-Arguments)
    - [Required Arguments](#Required-Arguments)
    - [Keyword Arguments](#Keyword-Arguments)
    - [Variable Number of Arguments](#Variable-Number-of-Arguments)
- [Python Lamba functions](#Python-Lamba-functions)
- [Functional Programming Tools](#Functional-Programming-Tools)
    - [The `map()` Function](#The-map-Function)
    - [The `filter()` Function](#The-filter-Function)
    - [The `reduce()` Function](#The-reduce-Function)
- [Class Exercise A](#Class-Exercise-A)
- [Class Exercise B](#Class-Exercise-B)
- [Class Exercise C](#Class-Exercise-C)
- [Class Exercise D](#Class-Exercise-D)

----------------------------------



## Python Functions

Functions are an essential part of the Python programming language,
whether the functions are built-in to the Python language or whether
they are accessed from other library modules (packages).
However, writing your own user-defined functions is a key skill that
all programmers are required to have.
Functions in programming consist of a set of instructions that can
be used repeatedly and typically, because of their complexity, are
better self-contained in a sub-program and called when needed.
This means that a user-defined function is a named block of code
that is written to carry out a specified task, often accepting one or
more input values and that may return values.

There are three types of functions in Python:
1. Built-in functions, such as `print()`, `str()`, `input()`, `int()`, etc.
2. User-Defined Functions (UDFs), which are functions that users
   create to accomplish some specific task, and
3. Anonymous functions, which are also called lambda functions because
   they are not declared with the standard def keyword.

Defining user-defined functions (UDF's) in Python:
There are four steps to defining a function in Python.
1. The keyword `def` is used to declare the function followed by the
   function name.
2. Arguments may be added to the function enclosed within parentheses
   and terminated with the colon `:` character
3. Then, statements (lines of code) are added to the function, and
4. The function may add a return statement if a value(s) are
   required to be sent back to the calling program.
   
NOTE: While a return statement is optional, without it, UDF's
	 will return an object `None`.

For example, the code below provides a solution to Lecture #2 Part A
```
def compute_primes(lower, upper):
   total_primes = 0
   for num in range(lower, upper + 1):
      # prime numbers are greater than 1
      if num > 1:
        for i in range(2, num):
            if(num % i) == 0 :
            break
        else:
            print(num, end=" ") only displays if for loop runs to completion
            without a break;
            total_primes += 1
   return total_primes

lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")
print("\ntotal primes...",  compute_primes(lower, upper))
```

### Function Arguments in Python

Function arguments refer to the data supplied when invoking a
function, whereas the names of the variables within the function
are referred to as parameter names.


There are four types of arguments that Python UDFs may accept:

#### Default Arguments
Default arguments are those that take a default value if no
argument value is passed during the function call. Default values
may be supplied using the assignment operator `=`.

Example `my_sum` function
```
def my_sum(a, b = 2):
   return a + b
```
Call `my_sum()` with only 1 parameter
```
print("my sum is: ", my_sum(5))
```
Call `my_sum()` with 2 parameters
```
print("my sum is: ", my_sum(5,  3))
```

#### Required Arguments
In Python, UDF required arguments MUST be present in a function
call, and MUST be specified in exactly the right order.

Here, both `variable_a` is a required argument.  `variable_b` will have the default value of `"pancake"`
```
def my_function(variable_a, variable_b = "pancakes):
   return variable_a, variable_b
```

#### Keyword Arguments
When defining UDF's, to make sure that all the arguments are supplied
in the right order, the parameter's keywords may be used when invoking
the function. These are used to identify the arguments by their
parameter name.

NOTE: By using the keyword arguments, the order of parameters may be
      switched without affecting the result!
For example
```
def my_diff(firstArg, secondArg = 2):
   return firstArg - secondArg
```
Call the function
```
print("my_diff is: ", my_diff(firstArg = 9, secondArg = 5))
print("my_diff is: ", my_diff(secondArg = 5, firstArg = 9))
```

#### Variable Number of Arguments
In situations where the exact number of arguments may not be known
or if a variable number of arguments are required to be passed,
Python allows for a variable number of arguments to be supplied
by using the `*pargs` syntax.
The asterisk (*) is placed before the variable name that holds the
values of all variable  nonkeyword positional arguments.

For example, define the `improved_sum()` function to accept a variable number of arguments
```
def improved_sum(*pargs):
   sum = 0
   for i in pargs:
      sum += i
   return sum
```
Calculate the sum
```
print("improved_sum: ",  improved_sum(1, 4, 5,  99))
```

Note that `pargs` passed into the function is of type `tuple`


Python also allows for a variable number of keyword arguments, typically defined using `**kwargs`.  The double asterisk (**) is placed before the variable name that contain values of all keyword arguments.   Here is an example with variable keyword arguments:
```
def another_improved_sum(**kwargs):
    sum = 0
    print("input keyword arguments", kwargs)
    for (k, v) in kwargs.items():
        sum += v
    return sum
```
Calculate sum:
```
print(another_improved_sum(a=2, b=2))
```

Note that `kwargs` passed into the function is of type `dict`

## Python Lamba functions

In Python, The `lambda` operator or lambda function is used as a way
to create small anonymous functions (i.e. functions without a name).
Lambda functions are:
- throw-away functions, (i.e. they are just needed
where they have been created).
- typically used when a nameless function is
required for a short period of time.
- mainly used in combination with the functions:
`filter()`, `map()` and `reduce()`.
- generally used as an argument to a
higher-order function (a function that takes in other functions as arguments).

While normal functions are defined using the `def` keyword, Python
anonymous functions are defined using the `lambda` keyword.

The general syntax of a lambda function is quite simple:
```
lambda argument_list : expression
```
alternately:
```
lambda argument1, argument2, ..., argumentN : expression using argument
```

The argument list consists of a comma separated list of arguments
and the expression is an arithmetic expression that uses these arguments.  Recall from [Lecture 1](lecture01.md)
expressions make use of arithmetic, relational, logical, bitwise, assignment, and special operators

You can assign the function to a variable to give it a name.
The following example of a lambda function returns the sum of its two
arguments:
```
my_lambda_function = lambda x, y : x + y
result = my_lambda_function(3, 6)
print(result) # displays 9
```
Equivalent using `def`
```
def my_def_function(x, y):
    return x + y
result = my_def_function(3, 6)
print(result) # displays 9
```

The function object returned by `lambda` work in the same way as those defined with `def`.  However, there are two main differences that give `lambda`s a unique role:

1. **`lambda` is an expression, not a statement**.  `lambda` expressions return a value (a new function) that can optionally be assigned a name.  The `def` statement always
assigns the new function to the name in the header, instead of returning it as a
result 
1.  **`lambda`’s body is a single expression, not a block of statements**. The lambda’s
body is limited to simple coding constructs that do not make use of full statements like those found in a `def` body’s return statement except that `lambda`'s

In short, `lambda` is designed for coding simple functions and `def` handles complex tasks.

## Functional Programming Tools

Python provides support for multiple programming paradigms: procedural (with its basic statements), object-oriented (with its classes), and functional. For the latter of these, Python includes a set of built-ins functions that operate on sequences and other iterables. This set
includes tools that:

- operate on an iterable’s items (`map`); 
- filter out iterable items based on a test function (`filter`); 
- apply a functions to pairs of iterable items and running results to produce a single cumulative result (`reduce`).

Essentially `map`, `filter`, `reduce` work similar to a `for` loop that iterates over a sequence (or iterable) to manipulate each element.

### The `map()` Function

The `map()` function takes an input sequence, transforms each element, and outputs an iterable.
`map()` is a function with two arguments:
```
r = map(func, seq)
```

The first argument `func` is the name of a function and the second
argument `seq` is a sequence (e.g. a list). The `map()` function
applies the function `func` to all the elements of the sequence `seq`.
`map()` returns an iterable map object with the elements changed by the function
`func`.  The signature of `func` should match `seq`

`map()` will apply the provided `func` to the elements of the argument list,
(i.e. it first applies to the elements at index 0, then to the elements at index 1,
until the n-th index is reached

For example, to double the value of a sequence:
```
a_list = [1, 2, 3, 4]

def double(x):
    return 2*x

map_result = map(double, a_list) # map_result is an iterable
print(map_result)

print(list(map_result)) # list() to create list from iterable
```

The advantage of the `lambda` operator can be seen when it is used in
combination with the `map()` function to produce more compact code.
```
map_result = map(lambda x: 2*x, a_list))
print(list(map_result))
```

`map()` can be applied to more than one list, however, the lists should have the same length. 

```
a_list = [1, 2, 3, 4]
b_list = [17, 12, 11, 10]
c_list = [-1, -4, 5]
```
```
m1 = map(lambda x, y : x + y, a, b)            # displays [18, 14, 14, 14]
print(list(m1)) # must display as a list because map() returns an iterable
```

In the example above, `lambda x, y : x + y` is the lambda function taking two arguments `x` and `y`.  
The expression `x + y` is evaluated and its value returned.

The function itself has no name (ie anonymous) and temporary. It returns a function object which
is assigned to the identifier `m1`.

This lambda function takes in three arguments
```
m2 = map(lambda x, y, z : x + y + z, a_list, b_list, c_list)  # what is this result?
print(list(m2))
```

### The `filter()` Function

As with the `map()` function, the `filter()` function in Python also accepts
a function and a sequence as arguments.

The `filter()` function offers an elegant way to filter out all the elements
of a sequence for which the function returns `True`

```
r = filter(func, seq)
```
`filter` applies `func` to each element in `seq` and returns `True` or `False`.  
Elements that returns `False` will be excluded in the returned iterator `r`

`filter()` returns an iterable filter object

In the example below, the filter() function is used to to filter out
only even numbers from a list.

```
random_list = [1, 5, 4, 6, 8, 11, 3, 12, 11, 9, 88]

def is_even_number(x):
    return (x % 2 == 0) # True for even numbers

even_result = filter(is_even_number , random_list)
print(even_result)

print(list(even_result))    # displays[4, 6, 8, 12, 88]
```

Similar with `map()` using an anonymous function results in more compact and readble code:
```
even_list = list(filter(lambda x : (x % 2 == 0) , random_list))
print(even_list)    # displays[4, 6, 8, 12, 88]
```

Here we apply a filter to produce odd numbers:
```
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x : x % 2, fibonacci))  # x % 2 is True for odd numbers
print(odd_numbers)
```

### The `reduce()` Function
```
reduce(func, seq)
```
The `reduce()` function repeatedly applies the function `func` to the sequence `seq` and returns a single value. 
`reduce()` is part of the `functools` module.

The signature of `func` takes in two arguments and returns a single value of the same type.

For `seq = [ s1, s2, s3, ... , sn ]`, calling `reduce(func, seq)` works as follows:
- The first two elements of `seq` will be passed to `func`
(i.e. `func(s1, s2)` ). The list on which `reduce()` works, now is:
`[ func(s1, s2), s3, ... , sn ]`
- In the next step func will be applied on the previous result and the
third element of the list (i.e. `func(func(s1, s2),s3)` )
- The list now looks like: `[ func(func(s1, s2), s3), ... , sn ]`
- This process continues until just one element is left and this element
is ultimately returned.

Example, to sum all values in a list:
```
from functools import reduce
a_list = [1, 2, 3, 4]

def my_sum(x,y):
    return x+y

sum_result = reduce(my_sum, a_list)
print(sum_result)
```
Same result using anonymous function:
```
from functools import reduce
sum_result = reduce(lambda x,y: x+y, a_list)
print(sum_result)
```

Example, to determine the largest value in a list:
```
from functools import reduce
def get_largest(a,b):
    return a if (a > b) else b

result = reduce(get_largest, [47, 115, 42, 102, 13])
print(result) # displays 115
```

Here, we give the anonymous function the name `func` by assigning the result of `lambda` to a variable
```
from functools import reduce
func = lambda a, b : a if (a > b) else b
result = reduce(func, [47, 115, 42, 102, 13])
print(result) # displays 115
```

Another way of coding the above:
```
from functools import reduce
result = reduce(lambda a, b : a if (a > b) else b, [47, 115, 42, 102, 13])
print(result) # displays 115
```

Example, calculating the sum of the numbers from 1 to 100:
```
print(reduce(lambda x, y : x + y, range(1, 101)))
```

## Class Exercise A
Write a function that returns the number of positional arguments, keyword arguments that was provided to it


## Class Exercise B
Write the code for a Python program that asks the user to enter
a whole number representing a number of terms of powers of 2 to
display and then uses an anonymous (lambda) function along with the
`map()` built-in function to compute and displays the powers of 2.
So that, if the user enters 10, then your program would display:
```
Total terms is: 10
2 raised to power 0 is 1
2 raised to power 1 is 2
2 raised to power 2 is 4
2 raised to power 3 is 8
2 raised to power 4 is 16
2 raised to power 5 is 32
2 raised to power 6 is 64
2 raised to power 7 is 128
2 raised to power 8 is 256
2 raised to power 9 is 512
```

## Class Exercise C
Use the `reduce()` to calculate the product (the factorial) from
1 to a number (up to 100).

## Class Exercise D
Given the following list of 3 records (each containing 4 fields):
```
item:         book:                           qty:      price:
34587         Learning Python, Mark Lutz      4         40.95
98762         Programming Python, Mark Lutz   5         56.80
77226         Head First Python, Paul Barry   3         32.95
```
Write a Python program, which returns a list with 2 tuples
`(book, price)` given the item #. The Python program must use
`lambda` and `map`.

