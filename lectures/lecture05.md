<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lecture #5
Monday June 6, 2022

## Lecture Objective

- Gain a high-level understanding of object oriented programming
- Familiarity with reading and using Python classes
- Introduction to data science tools in Python

## Pre-requisites

- Python version 3.9.9 installed on your computer and on Raspberry Pi
    check Python version with `python -V`

## Page Contents

- [Introduction to Python Object Oriented Programmimg](#Introduction-to-Python-Object-Oriented-Programmimg)
   - [Overview of OOP Terminology](#Overview-of-OOP-Terminology)
   - [Creating Classes in Python](#Creating-Classes-in-Python)
   - [`Employee` class example](#Employee-class-example)
   - [Creating Instance Objects in Python](#Creating-Instance-Objects-in-Python)
   - [Accessing Attributes and Methods](#Accessing-Attributes-and-Methods)
   - [Python Built-In Class Attributes](#Python-Built-In-Class-Attributes)
   - [Destroying Python Objects (via Garbage Collection)](#Destroying-Python-Objects-via-Garbage-Collection)
   - [Python Operator Overloading](#Python-Operator-Overloading)
   - [Class to represent a point on a 2D Plane](#Class-to-represent-a-point-on-a-2D-Plane)
- [Class Exercise A](#Class-Exercise-A)
- [Class Exercise B](#Class-Exercise-B)
- [Class Exercise C](#Class-Exercise-C)

----------------------------------

## Introduction to Python Object Oriented Programmimg
Python is a multi-paradigm programming language, that supports
different programming approaches.
A popular approach to solving programming problems is to create
and use objects.
This approach is known as Object-Oriented Programming, or (OOP).
The goal of OOP in Python (and other languages) is to focus on creating
reusable code that parallels how objects work in "real life" scenarios.

Python has been an object-oriented programming language from conception.

## Overview of OOP Terminology
Class:         A user-defined prototype for an object that defines a set of
               attributes and methods that characterize any object of the class.
               The attributes are data members (class variables and instance variables)
               and methods are functions. Both are accessed via dot (member) notation.

|Term            | Description |
|:---------------|:---------------------------------------------------------------
|Class variable | A variable that is shared by all instances of a class. Class variables are defined within a class but outside any of the class's methods. |
| Data member | A class variable or instance variable that holds data associated with a class and its objects. |
| Function overloading| The assignment of more than one behavior to a particular function. The operation performed varies by the types of objects or arguments involved. |
| Instance variable |A variable that is defined inside a method and belongs only to the current instance of a class. |
| Inheritance | The transfer of the characteristics of a class to other classes that are derived from it. |
| Instance | An individual object of a certain class. An object 'x1' that belongs to a class Circle, for example, is an instance of the class Circle. |
| Instantiation | The creation of an instance of a class. |
| Method | A special kind of function that is defined in a class definition. |
| Object | A unique instance of a data structure that's defined by its class.  An object comprises both data members (class variables and instance variables) and methods (functions). |
| Operator overloading | The assignment of more than one function to a particular operator. Operator overloading is used to allow primitive operators (+, -, *, /, etc) to work with objects as they  would with primitive types. |

## Creating Classes in Python
The keyword `class` is used to create a new class definition. The name of the
class immediately follows the keyword class followed by a colon as follows:
```
class ClassName:
   '''optional class documentation string'''
   # If a class/method has a documentation string, it may be accessed
   # via ClassName.__doc__

   # data and methods go here...
   # The component defining the class members (i.e.) data attributes and functions.
```
## `Employee` class example
```
class Employee:
   '''common base class for all employees'''
   emp_count = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.emp_count += 1 # global increment for all objects

   def displayCount(self):
     print("Total Employees %d" % Employee.emp_count)

   def displayEmployee(self):
      print("Name:", self.name,  ", Salary:", self.salary)
```

- The variable `emp_count` is a class variable whose value is shared among
all instances of this class. This can be accessed as `Employee.emp_count`
from inside or outside of the class.
- The first method `__init__()` is a special method, which is called
a class constructor or initialization method that Python calls when
creating a new instance of this class.
- Other class methods may be created as functions, except that the
first argument to each method must be the keyword `self`.
- Python adds the `self` argument to the method call automatically
which acts as a reference to the current object in memory.

## Creating Instance Objects in Python
To create instances of a class, the class name is used and accepts
any arguments as required its `__init__` method accepts.

In the example below, `MyClass` takes two arguments when creating instances
```
class MyClass:
   def __init__(self, param1, param2):
      pass
   
   ...

```

## Accessing Attributes and Methods
Access to the object's attributes and methods are accomplished by using the
dot operator (`.`) on an object. A class variable would be accessed using class name
followed by the variable.

Example:
```
emp1 = Employee("Bill Gates", 123456789.99)
emp2 = Employee("Steve Wozniak", 23456789.99)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employees %d" % Employee.emp_count)
```

Class attributes may be added, removed, or modified at any point within
the Python program!
```
emp1.age = 7  # Add an 'age' attribute.
emp1.age = 8  # Modify 'age' attribute.
del emp1.age  # Delete 'age' attribute.
```

In place of using direct statements to access attributes, the
following functions may be used:
|Method           | Description                |
|:----------------|:---------------------------|
| `getattr(obj, name[, default])` | access the attribute of an object. |
| `hasattr(obj, name)` | check if an attribute exists. |
| `setattr(obj, name, value)` | set an attribute, and if the attribute does not exist, it is created. |
| `delattr(obj, name)` | to delete an attribute. |

Examples:
```
hasattr(emp1, 'age')     # Returns true if the 'age' attribute exists
getattr(emp1, 'age')     # Returns value of the 'age' attribute
setattr(emp1, 'age', 19) # Set attribute 'age' to 19
delattr(empl, 'age')     # Delete attribute 'age'
```

## Python Built-In Class Attributes
Every Python class keeps following built-in attributes that can be
accessed using the dot operator:
|Attribute        | Description                |
|:----------------|:---------------------------|
| __dict__ | Dictionary containing the class's namespace. |
| __doc__ | Class documentation string or none, if undefined. |
| __name__ | Class name. |
| __module__ | Module name in which the class is defined. This attribute is "__main__" in interactive mode. |


## Destroying Python Objects (via Garbage Collection)
Python deletes unused objects (built-in types or class instances) automatically
to free up memory. The process by which Python periodically reclaims blocks of
memory that are no longer are in use is termed _Garbage Collection_.

Python's garbage collector runs during program execution and is triggered when
an object's reference count reaches zero. An object's reference count changes as
the number of aliases that point to it change.

An object's reference count increases when it is assigned a new name or placed in
a container (list, tuple, or dictionary). The object's reference count decreases
when it's deleted with `del`, its reference is reassigned, or its reference goes
out of scope. When an object's reference count reaches zero, Python collects it
automatically.

The Python garbage collector destroys an orphaned instance and reclaims its space
automatically, but a class can implement the special method `__del__()`, called a
destructor, that is invoked when the instance is about to be destroyed.
This method may be used to clean up any non memory resources used by an instance.

## Python Operator Overloading

To overload operators (+, -, *, /, etc) to work with objects in the same
way that primitive variables do, the special `__func__()` functions must be used.

The function names are listed below:

| operation:     | example: |  function name: |
|:---------------|:---------|:-----------|
| Addition       | p1 + p2  |  `__add__()` |
| Subtraction    | p1 - p2  |  `__sub__()` |
| Multiplication | p1 * p2  |  `__mul__()` |
| Exponent       | p1 ** p2 |  `__pow__()` |
| Division       | p1 / p2  |  `__truediv__()` |
| Floor Division | p1 // p2 |  `__floordiv__()` |
| Remainder      | p1 % p2  |  `__mod__()` |
| Left Shift     | p1 << p2 |  `__lshift__()` |
| Right Shift    | p1 >> p2 |  `__rshift__()` |
| Bitwise AND    | p1 & p2  |  `__and__()` |
| Bitwise OR     | p1 \| p2  |  `__or__()` |
| Bitwise XOR    | p1 ^ p2  |  `__xor__()` |
| Bitwise NOT    | ~p1      |  `__invert__()` |
| Less than      | p1 < p2  |  `__lt__()` |
| Less-than-or-equal | p1 <= p2 |  `__le__()` |
| Equals       | p1 == p2 |  `__eq__()` |
| Not-equal   | p1 != p2  | `__ne__()` |
| Greater-than  | p1 > p2  |  `__gt__()` |
| Greater-than-or-equal | p1 >= p2 |  `__ge__()` |

## Class to represent a point on a 2D Plane
```
import math

class Point:
   # docstrings can be accessed for help with a class description
   # by accessing __doc__ within a class/method
   '''      
      This class represents a point in a two-dimensional plane
   '''

   def __init__(self, x=0, y=0, copy=None):
   '''
      This constructor initializes the position of a new point
      The x and y coordinates can be specified, but default to 0, 0.
   '''
      if copy != None:
         self.move(copy.x, copy.y)
      else:
         self.move(x, y)

   def __str__(self):
      return "({0},{1})".format(self.x, self.y)

   def move(self, x, y):
      '''
         The move(self, x, y) function moves the point to a new location in 2D space.
      '''
      self.x = x
      self.y = y

   def reset(self):
      '''
         The reset(self) function, sets the point back to the origin: 0, 0
      '''
      self.move(0, 0)

   def distance(self, other_point):
      '''
         The distance(self, other_point) function calculates the distance from the
         current instance of point to a second point passed as a parameter.
         This function uses the Pythagorean Theorem to calculate
         the distance between the two points. The distance is
         returned as a float.
      '''
      return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

   def __add__(self, rhs):
      x_add = self.x + rhs.x
      y_add = self.y + rhs.y
      return Point(x_add, y_add)

   def __del__(self):
      print("destroying Point class...", self)
```

Using the `Point` class:
```
print(Point.__doc__)
print(Point.__init__.__doc__)
point1 = Point()            # create 2 Point objects
point2 = Point()

print(Point.reset.__doc__)
point1.reset()

print(Point.move.__doc__)
point2.move(5,0)

print(Point.distance.__doc__)
print(point2.distance(point1))

point1.move(3,4)
print(point1.distance(point2))
print(point1.distance(point1))

point3 = point1 + point2
print(point3)
print(point2)

point4 = Point(point2)
print("New point4 is:", point4)
```


## Class Exercise A

Examine class structure for [Yahoo! Finance's API](https://github.com/ranaroussi/yfinance) and provide a list of methods the `Ticker` class implements


## Class Exercise B

Write code to use the `yfinance` library to collect closing price on 31-May-2022 for the following tickers:
- `IBM` (International Business Machines, NYSE)
- `RY` (Royal Bank of Canada, TO)

## Class Exercise C

Create a Jupyter notebook to 
- load daily data for stock ticker 'AAPL' between 01-Jan-2021 and 31-Dec-2021
- plot daily close price
- plot daily volume
- calculate the monthly average price
