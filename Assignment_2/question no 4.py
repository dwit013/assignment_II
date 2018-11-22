#Write a Python program to multiply each item in a list by an integer.

#code

list = []

i=0

val = int(input("Enter number of elements for list: "))

for j in range (0, val):
    x = int(input("Enter numbers for list: "))
    list.append(x)

value = int(input("Enter the value for the multiple: "))

for y in list:
    list[i] = list[i] * value
    i=i + 1

print(list)
