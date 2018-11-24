#!/usr/bin/env python3
"""
@author: Salwa Ahmed
"""


# function to find if
# given point lies inside
# a given rectangle or not.


def FindPoint(x1, y1, x2,
              y2, x, y):
    if ((x > 1 or x == 1) and (x < 5 or x == 5) and
            (y > 1 or y == 1) and (y < 6 or y == 6)):
        return "New York"
    if ((x > 10 or x == 10) and (x < 13 or x == 13) and
                (y > 1 or y == 1) and (y < 2 or y == 2)):
        return "Paris"
    if ((x > 100 or x == 100) and (x < 78 or x == 78) and
                (y > 110 or y == 110) and (y < 82or y == 82)):
        return "London"
    else:
        return "the point is outside all"


# Driver code

if __name__ == "__main__":

    # bttom-left and top-right
    # corners of rectangle.
    # use multiple assigment
    x1, y1, x2, y2 = 1, 1, 5, 6

    # given point
    x, y = 2, 1

    # function call

    print( FindPoint(x1, y1, x2,
                 y2, x, y))



