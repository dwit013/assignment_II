#   Name: Abhishek Pandey
#   Roll no: 706

# 7. Write a Python program to insert a given string at the beginning of all items in a list. 
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

list = [1,2,3,4]
list2 =['emp{0}'.format(i) for i in  list]

print(list2)


