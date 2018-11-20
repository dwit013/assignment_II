'''

7. Write a Python program to insert a given string at the beginning of all items in a list.
Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

'''

num = [25,23,12,34,13]
print("list before adding emp",num)

print("list after adding emp",['emp{0}'.format(i) for i in num])
