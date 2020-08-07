#!/usr/bin/python

class Rect(object):
    def __init__(self, length, width, x=0, y=0):
        self._length = length
        self._width = width
        self._x = x
        self._y = y

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return (self._length + self._width) * 2
    
    def pos(self):
        return {self._x : self._y}

    def move(self, x, y):
        self._x = x
        self._y = y

def main():
    rect = Rect(10, 20)
    print(f'rectangle area: {rect.area()}')
    print(f'rectangle perimeter: {rect.perimeter()}')
    rect.move(100, 50)
    print(f'rectangle position: {rect.pos()}')

if __name__ == '__main__':
    main()
