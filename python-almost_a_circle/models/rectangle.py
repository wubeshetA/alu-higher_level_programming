#!/usr/bin/python3
"""Script with implementation of rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Represent rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize the rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
            Returning private attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set private attribute width
        """
        self.__width = value

    @property
    def height(self):
        '''
            Returning private attribute
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''
            Setting private attribute
        '''
        self.__height = value

    @property
    def x(self):
        '''
            Returning private attribute
        '''
        return self.__x

    @x.setter
    def x(self, value):
        '''
            Setting private attribute
        '''
        self.__x = value

    @property
    def y(self):
        '''
            Returning private attribute
        '''
        return self.__y

    @y.setter
    def y(self, value):
        '''
            Setting private attribute
        '''
        self.__y = value
