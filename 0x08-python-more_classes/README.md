# 0x08. Python - More Classes and Objects

-   [Object Oriented programming](https://intranet.alxswe.com/rltoken/M-MFweENpRdEfRto_Gzlvg)
-   [Class and instance Attributes](https://intranet.alxswe.com/rltoken/SGQIevRxW6lTgr4jGDzXbw)
-   [classmethods and staticmethods](https://intranet.alxswe.com/rltoken/Ij1EnTg02gtIknOkNv4xGA)
-   [Getters vs Setters](https://intranet.alxswe.com/rltoken/xjpk-jUNe0uGEzcNXbwIHQ)
-   [str vs repr](https://intranet.alxswe.com/rltoken/iu1ILT-t6FMuZvk7vRvfuQ)

## Tasks

0. ### Simple Rectangle
    Write an empty class Rectangle that defines a rectangle:

-   You are not allowed to import any module

1.  ### Real definition of a rectangle

    Write a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)

    -   Private instance attribute: `width:`
        property `def width(self):` to retrieve it
        property setter `def width(self, value):` to set it:
        -   `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
        -   if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
    -   Private instance attribute: `height`:
        -   property `def height(self):` to retrieve it
        -   property setter `def height(self, value):` to set it:
            -   `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
            -   if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
        -   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`

2.  ### Area and Perimeter

    Write a class Rectangle that defines a rectangle by: (based on 1-rectangle.py)

    -   Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
    -   Public instance method: `def area(self):` that returns the rectangle area
    -   Public instance method: def perimeter(self): that returns the rectangle perimeter:
        -   if `width` or `height` is equal to `0`, perimeter is equal to `0`

3.  ### String representation

    Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)

    -   `print()` and `str()` should print the rectangle with the character #: (see example below)
        -   if width or height is equal to 0, return an empty string
    -   You are not allowed to import any module

    ```bash
    guillaume@ubuntu:~/0x08$ cat 3-main.py
    #!/usr/bin/python3
    Rectangle = __import__('3-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

    print(str(my_rectangle))
    print(repr(my_rectangle))

    print("--")

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle)
    print(repr(my_rectangle))

    guillaume@ubuntu:~/0x08$ ./3-main.py
    Area: 8 - Perimeter: 12
    ##
    ##
    ##
    ##
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    --
    ##########
    ##########
    ##########
    <3-rectangle.Rectangle object at 0x7f92a75a2eb8>
    guillaume@ubuntu:~/0x08$
    ```

4.  ### Eval is magic

    Write a class Rectangle that defines a rectangle by: (based on 3-rectangle.py)

    -   `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (**see example below**)
    -   You are not allowed to import any module

    ```bash
    guillaume@ubuntu:~/0x08$ cat 4-main.py
    #!/usr/bin/python3
    Rectangle = __import__('4-rectangle').Rectangle

    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))

    guillaume@ubuntu:~/0x08$ ./4-main.py
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7cc88
    --
    ##
    ##
    ##
    ##
    --
    ##
    ##
    ##
    ##
    --
    Rectangle(2, 4)
    --
    0x7f09ebf7ccc0
    --
    False
    True
    guillaume@ubuntu:~/0x08$
    ```

5.  ### Detect instance deletion

    Write a class Rectangle that defines a rectangle by: (based on 4-rectangle.py)

    -   Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
    -   You are not allowed to import any module

6.  ### How many instances

    Write a class Rectangle that defines a rectangle by: (based on 5-rectangle.py)

    -   Public class attribute number_of_instances:
        -   Initialized to 0
        -   Incremented during each new instance instantiation
        -   Decremented during each instance deletion

7.  ### Change Representation

    Write a class Rectangle that defines a rectangle by: (based on 6-rectangle.py)

    -   Public class attribute print_symbol:
        -   Initialized to #
        -   Used as symbol for string representation
        -   Can be any type

8.  ### Compare rectangles

    Write a class Rectangle that defines a rectangle by: (based on `7-rectangle.py`)

    -   Static method `def bigger_or_equal(rect_1, rect_2)`: that returns the biggest rectangle based on the area

        -   `rect_1` must be an instance of Rectangle, otherwise raise a `TypeError` exception with the message `rect_1` must be an instance of `Rectangle`
        -   `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2` must be an instance of `Rectangle`
        -   Returns `rect_1` if both have the same area value

9.  ### A square is a rectangle

    Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

    -   Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
