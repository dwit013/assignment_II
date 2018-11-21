#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']
 
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','Purple','Blue']
print("The list is",list)

list.pop(0)
list.pop(4)
list.pop(5)

print("The list after removing the0th 4th and 5th element is: ",list)
