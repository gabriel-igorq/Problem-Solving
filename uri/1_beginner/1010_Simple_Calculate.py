code_1, units_1, price_1 = input().split()
code_1, units_1, price_1 = [int(code_1), int(units_1), float(price_1)]

code_2, units_2, price_2 = input().split()
code_2, units_2, price_2 = [int(code_2), int(units_2), float(price_2)]


print(f'VALOR A PAGAR: R$ {units_1*price_1 + units_2*price_2:.2f}')