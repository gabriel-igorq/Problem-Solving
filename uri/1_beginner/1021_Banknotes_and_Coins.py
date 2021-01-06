"""
Read a value of floating point with two decimal places. This represents a monetary value.
After this, calculate the smallest possible number of notes and coins on which the value can be decomposed.
The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01.
Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.
"""

value = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for i in notes:
    number_of_notes = int(value/i)
    value -= number_of_notes*i
    print(f'{number_of_notes} nota(s) de R$ {i}.00')

print('MOEDAS:')
for i in coins:
    value = round(value, 2)
    number_of_coins = int(value/i)
    value -= number_of_coins * i
    print(f'{number_of_coins} moeda(s) de R$ {i:.2f}')