'''
6. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

'''
list1 = [1,2,3,4,5,6,7,8,9]

print("List before items removed",list1)

list1.pop(0)
list1.pop(4)
list1.pop(5)

print("list after the removal of 0th 4th and 5th item: ",list1)
