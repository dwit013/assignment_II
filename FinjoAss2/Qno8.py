'''
8. Write a Python program to remove duplicates from a list.
'''

someList=[23,43,33,23,12,13,13,13,67,89,89]
newList=[]

for item in someList:
    if item not in newList:
        newList.append(item)


print(newList)
