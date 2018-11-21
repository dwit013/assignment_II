# 2.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a
# string. If the string length is less than 2, return “Empty String”.

str = 'apple'

if len(str) < 2:
    print('empty string')
else:
    str[:2]+str[-2:]
