""" Write a Python program to insert a given string at the beginning of all items
in a list. 
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4'] """

#code

list = [1,2,3,4]

i=0

value = input('Enter the string: ')

for y in list:
    list[i]= value + str(list[i])
    i=i + 1

print(list)
