<h1>0x0A. <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" alt="logo python" width="30" height="30">Python - Inheritance </h1>

![Inheritance img](https://mytoshika.com/blog/wp-content/uploads/2019/06/Types_Of_Inhertiance_In_Java.jpg)
## Resources
### Read or watch:

- Inheritance
- Multiple inheritance
- Inheritance in Python
- Learn to Program 10 : Inheritance Magic Methods

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

## General
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use isinstance, issubclass, type and super built-in functions

## Requirements
## Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 - LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- Python Test Cases
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## More Info
## Shoutouts
Justin Marsh for the “Python 3 Object-oriented Programming” book rec

# Tasks

## 0. Lookup mandatory
Write a function that returns the list of available attributes and methods of an object:

- Prototype: def lookup(obj):
- Returns a list object
- You are not allowed to import any module  
***Output:***
```
❯ ./0-main.py
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'my_attr1', 'my_meth']
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
```

## 1. My list mandatory
Write a class MyList that inherits from list:

- Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
- You can assume that all the elements of the list will be of type int
- You are not allowed to import any module  
***Output:***
```
❯ ./1-main.py
[1, 4, 2, 3, 5]
[1, 2, 3, 4, 5]
[1, 4, 2, 3, 5]
```

## 2. Exact same object mandatory
Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

- Prototype: def is_same_class(obj, a_class):
- You are not allowed to import any module  
***Output:***
```
❯ ./2-main.py
1 is an instance of the class int
```

## 3. Same class or inherit from mandatory
Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

- Prototype: def is_kind_of_class(obj, a_class):
- You are not allowed to import any module  
***Output:***
```
❯ ./3-main.py
1 comes from int
1 comes from object
```

## 4. Only sub class of mandatory
Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

- Prototype: def inherits_from(obj, a_class):
- You are not allowed to import any module  
***Output:***
```
❯ ./4-main.py
True inherited from class int
True inherited from class object
```

## 5. Geometry module mandatory
Write an empty class BaseGeometry.

- You are not allowed to import any module  
***Output:***
```
❯ ./5-main.py
<5-base_geometry.BaseGeometry object at 0x7fe23fe183d0>
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
```

## 6. Improve Geometry mandatory
Write a class BaseGeometry (based on 5-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- You are not allowed to import any module  
***Output:***
```
❯ ./6-main.py
[Exception] area() is not implemented
```

## 7. Integer validator mandatory
Write a class BaseGeometry (based on 6-base_geometry.py).

- Public instance method: def area(self): that raises an Exception with the message area() is not implemented
- Public instance method: def integer_validator(self, name, value): that validates value:
you can assume name is always a string
    - if value is not an integer: raise a TypeError exception, with the message <name> must be an integer
    - if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
- You are not allowed to import any module  
***Output:***
```
❯ ./7-main.py
[TypeError] name must be an integer
[ValueError] age must be greater than 0
[ValueError] distance must be greater than 0
```

## 8. Rectangle mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

- Instantiation with width and height: def __init__(self, width, height):
    - width and height must be private. No getter or setter
    - width and height must be positive integers, validated by integer_validator  
***Output:***
```
❯ ./8-main.py
<8-rectangle.Rectangle object at 0x7f47c46c83d0>
['_Rectangle__height', '_Rectangle__width', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
[AttributeError] 'Rectangle' object has no attribute 'width'
[TypeError] height must be an integer
```

## 9. Full rectangle mandatory
Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)

- Instantiation with width and height: def __init__(self, width, height)::
    - width and height must be private. No getter or setter
    - width and height must be positive integers validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>  
***Output:***
```
❯ ./9-main.py
[Rectangle] 3/5
15
```

## 10. Square #1 mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py):

- Instantiation with size: def __init__(self, size)::
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator
- the area() method must be implemented  
***Output:***
```
❯ ./10-main.py
[Rectangle] 13/13
169
```

## 11. Square #2 mandatory
Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

- Instantiation with size: def __init__(self, size)::
    - size must be private. No getter or setter
    - size must be a positive integer, validated by integer_validator
- the area() method must be implemented
- print() should print, and str() should return, the square description: [Square] <width>/<height>  
***Output:***
```
❯ ./11-main.py
[Square] 13/13
169
[Rectangle] 13/13
169
```


# Advanced Task

## 12. My integer
Write a class MyInt that inherits from int:

- MyInt is a rebel. MyInt has == and != operators inverted
- You are not allowed to import any module  
***Output:***
```
❯ ./100-main.py
3
False
True
```

## 13. Can I?
Write a function that adds a new attribute to an object if it’s possible:

- Raise a TypeError exception, with the message can't add new attribute if the object can’t have new attribute
- You are not allowed to use try/catch
- You are not allowed to import any module  
***Output:***
```
❯ ./101-main.py
John
[TypeError] can't add new attribute

```