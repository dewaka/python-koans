#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise TriangleError, "Bad side length"

    if not ((a*a + b*b >= c*c) or (b*b + c*c <= a*a) or (c*c + a*a <= b*b)):
        raise TriangleError, "Impossible triangle!"

    if a == b == c:
        return 'equilateral'    
    elif (a != b) and (b != c) and (c != a):
        return 'scalene'
    else:
        return 'isosceles'

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
