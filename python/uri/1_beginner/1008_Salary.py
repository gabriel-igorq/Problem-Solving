"""
Write a program that reads an employee's number, his/her worked hours number in a month and the amount he received
per hour. Print the employee's number and salary that he/she will receive at end of the month, with two decimal places.
"""

number = int(input())
hours = int(input())
amount_per_hour = float(input())

print(f'NUMBER = {number}')
print(f'SALARY = U$ {hours*amount_per_hour:.2f}')