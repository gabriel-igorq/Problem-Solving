"""
Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its
respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month.
In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364.
This is just an exercise for the purpose of testing simple mathematical reasoning.
"""

age_in_days = int(input())

years = age_in_days//365
age_in_days -= years*365

months = age_in_days//30
days = age_in_days % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')
