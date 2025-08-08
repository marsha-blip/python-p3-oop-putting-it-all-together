#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self._size = size
        self._color = None
        self._material = None
        self.condition = "Used"

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

