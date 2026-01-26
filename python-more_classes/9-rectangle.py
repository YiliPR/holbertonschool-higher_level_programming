#!/usr/bin/python3

class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width=width
        self.height=height
        Rectangle.number_of_instances += 1

        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            
            self.__width = value

        @property
        def height(self, value):
            return self.__height
        
        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            
            self.__height = value

    def area(self):
      a = self.width
      b = self.height
      return a * b


    def perimeter(self):
        if self.width or self.height != 0:
            return 2 * (self.width + self.height)
        if self.width or self.height == 0:
            return 0

    def __str__(self):
            waka = ""
            if self.width == 0 or self.height == 0:
                return ""
            elif self.width != 0 and self.height != 0:
                for i in range(self.height):
                    for j in range(self.width):
                        waka += str(self.print_symbol)
                    waka += "\n"
                return waka.rstrip()
            
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print ("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @classmethod
    def set_print_symbol(cls, value):
        if not isinstance(value, str) or value == "":
            raise ValueError ("Value needs to be a string")
        cls.print_symbol = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError ("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2,Rectangle):
            raise TypeError ("rect_2 must be an instance of Rectangle")
        
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1
        
    @classmethod
    def square(cls, size=0):
        return cls(size, size)
