"""
Read an integer value, which is the duration in seconds of a certain event in a factory,
and inform it expressed in hours:minutes:seconds.
"""
value = int(input())

hours = value//3600
value -= hours*3600

minutes = value//60
seconds = value - minutes*60

print(f'{hours}:{minutes}:{seconds}')
