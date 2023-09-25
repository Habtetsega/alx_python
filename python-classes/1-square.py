#!/usr/bin/python3
"""Defining class"""
class Square:
    """Representing a squre"""
    def __init__(self, size=0):
        if not isinstance(self, int):
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")
        self.__size = size
