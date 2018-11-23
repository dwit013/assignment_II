#Write a Python program to remove duplicates from a list.
list1=[1,2,3,7,8,9,3,2,1]
list2=[]
for num in list1:
    if num not in list2:
        list2.append(num)

print(list2)
