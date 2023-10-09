#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """
        Computes the area of the geometry.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclass must implement area() method.")

    def perimeter(self):
        """
        Computes the perimeter of the geometry.
        This method should be implemented by subclasses.
        """
        raise NotImplementedError("Subclass must implement perimeter() method.")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        Initializes a Rectangle object with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator(width, "width")
        self.integer_validator(height, "height")
        self.__width = width
        self.__height = height

    def integer_validator(self, value, name):
        """
        Validates that a value is a positive integer.

        Args:
            value: The value to be validated.
            name (str): The name of the value.

        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return self.__str__()


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square object with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            ValueError: If size is not a positive integer.
        """
        self.__size = 0
        self.integer_validator(size, "size")
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
