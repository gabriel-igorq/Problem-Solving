"""
Read three values (variables A, B and C), which are the three student's grades. Then, calculate the average,
considering that grade A has weight 2, grade B has weight 3 and the grade C has weight 5.
Consider that each grade can go from 0 to 10.0, always with one decimal place.
"""

A = round(float(input()), 1)
B = round(float(input()), 1)
C = round(float(input()), 1)

MEDIA = (2*A + 3*B + 5*C)/10

print(f'MEDIA = {MEDIA:.1f}')