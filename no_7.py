#Write a Python program to insert a given string at the beginning of all items in a list.
#Sample list : [1,2,3,4], string : emp
#Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
 
list = [1,2,3,4]

print("List before ",list)
list1=['emp{0}'.format(i) for i in list]
print("list after adding emp",list1)
