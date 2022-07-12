#!/usr/bin/python3
""" 4-main """
from models.base import Base


if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()  # !/usr/bin/python3
"""This rectangle inherits base"""


class Rectangle(Base):
    """This class has even weirder init"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """okay not that weird, just using Base id"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) == int and value > 0:
            self.__width = value
        elif type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) == int and value > 0:
            self.__height = value
        elif type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) == int and value >= 0:
            self.__x = value
        elif type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) == int and value >= 0:
            self.__y = value
        elif type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """returns area of a rectangle"""
        return self.height * self.width

    def display(self):
        """This method prints the rectangle, catering for x and y"""
        for y in range(self.y):
            print()
        while self.__height:
            print(' ' * self.__x, end='')
            print("#" * self.__width)
            self.__height -= 1

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args):
        """This method allows you to assign
            values to attributes of object
            rectangle by passing in arguments
            mapped to the rectangle attributes
        """
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            elif i == 4:
                self.__y = args[i]
