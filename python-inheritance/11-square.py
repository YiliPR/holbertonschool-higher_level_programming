#!/usr/bin/python3

Reactangle = __import__('9-rectangle').Rectangle

class Square(Reactangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size,size)

    def area(self):
        return super().area()

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
