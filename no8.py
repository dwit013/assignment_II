#Write a Python program to remove duplicates from a list.
list1=[1,2,3,9,11,7,3,4,1]
list2=[]
for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)
