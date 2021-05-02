"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes
in which the value may be decomposed. The possible banknotes are 100, 50, 20, 10, 5, 2 e 1.
Print the read value and the list of banknotes.
"""

value = int(input())
print(value)
notes = [100, 50, 20, 10, 5, 2, 1]

for i in notes:
    if value >= i:
        number_of_notes = int(value/i)
    else:
        number_of_notes = 0

    value -= number_of_notes*i
    print(f'{number_of_notes} nota(s) de R$ {i},00')

