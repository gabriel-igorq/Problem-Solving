"""
Make a program that calculates and shows the volume of a sphere being provided the value of its radius (R) .
The formula to calculate the volume is: (4/3) * pi * R3. Consider (assign) for pi the value 3.14159.
"""

R = float(input())

volume = 4/3*3.14159*R**3

print(f'VOLUME = {volume:.3f}')