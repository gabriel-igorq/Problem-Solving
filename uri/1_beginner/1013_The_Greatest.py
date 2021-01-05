"""
Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior".
Use the following formula:
MaiorAB = (a+b+abs(a-b))/2
"""

a, b, c = map(int, input().split())

maiorAB = (a+b+abs(a-b))/2
maior = (maiorAB + c + abs(maiorAB - c))/2

print(f'{maior:.0f} eh o maior')