# Write a Python program to multiply each item in a list by an integer.

a=5
lst=[1,2,3,4,5,6,7,8,9]

intr=list(map(lambda x: x*a,lst))

print(intr)