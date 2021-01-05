"""
Read the four values corresponding to the x and y axes of two points in the plane, p1 (x1, y1) and p2 (x2, y2)
and calculate the distance between them, showing four decimal places after the comma, according to the formula:

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
"""

from math import sqrt

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f'{distance:.4f}')