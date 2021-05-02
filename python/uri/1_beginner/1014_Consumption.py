"""
Calculate a car's average consumption being provided the total distance traveled (in Km)
and the spent fuel total (in liters).
"""

X = int(input())
Y = round(float(input()), 1)

print(f'{X/Y:.3f} km/l')