# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
a=input("enter 1st string: ")
b=input("enter 2nd string: ")

c=a[0:2]+b[2:]
d=b[0:2]+a[2:]

print(d+" "+c)
