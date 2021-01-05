"""
Make a program that reads a seller's name, his/her fixed salary and the sale's total made by himself/herself
in the month (in money). Considering that this seller receives 15% over all products sold,
write the final salary (total) of this seller at the end of the month , with two decimal places.
"""

name = input()
fixed_salary = float(input())
sales = float(input())

print(f'TOTAL = R$ {fixed_salary + sales*0.15:.2f}')