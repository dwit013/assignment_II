# Write a Python program to remove duplicates from a list


#code

list1 = ['Ramesh','Rohan','Rajesh',1,2,5,1,'Rohan']
list2 = []

for x in list1:
    if x not in list2:
        list2.append(x)

print(list2)


