#Write a Python program to insert a given string at the beginning of all items in a list.
#Sample list : [1,2,3,4], string : emp
#Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

mylist = [2, 4, 7, 8, "Heaven"]
init = "Emp"
i=0
for item in mylist:
    mylist[i] = init + str(item)
    i = i+1
print(mylist)
