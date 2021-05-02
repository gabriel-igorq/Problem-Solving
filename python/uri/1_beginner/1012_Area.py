"""
Make a program that reads three floating point values: A, B and C. Then, calculate and show:
a) the area of the rectangled triangle that has base A and height C.
b) the area of the radius's circle C. (pi = 3.14159)
c) the area of the trapezium which has A and B by base, and C by height.
d) the area of ​​the square that has side B.
e) the area of the rectangle that has sides A and B.
"""

# A, B, C = input().split()
# A, B, C = [round(float(A), 1), round(float(B), 1), round(float(C), 1)]

A, B, C = map(float, input().split())
pi = 3.14159

area_triangulo = A*C/2
area_circulo = pi*C**2
area_trapezio = (A+B)*C/2
area_quadrado = B*B
area_retangulo = A*B

print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')
