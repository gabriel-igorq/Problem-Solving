"""
In this problem, the task is to read a code of a product 1, the number of units of product 1,
the price for one unit of product 1, the code of a product 2, the number of units of product 2
and the price for one unit of product 2. After this, calculate and show the amount to be paid.
"""

code_1, units_1, price_1 = input().split()
code_1, units_1, price_1 = [int(code_1), int(units_1), float(price_1)]

code_2, units_2, price_2 = input().split()
code_2, units_2, price_2 = [int(code_2), int(units_2), float(price_2)]


print(f'VALOR A PAGAR: R$ {units_1*price_1 + units_2*price_2:.2f}')