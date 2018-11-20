'''
Qno3.
Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.

'''


string = input("enter the string: ")

a,b=string.split(" ")

a, b = a.replace(a[:2], b[:2]) , b.replace(b[:2], a[:2])

print(a+","+b)

