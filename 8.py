#   Name: Abhishek Pandey
#   Roll no: 706

# 8. Write a Python program to remove duplicates from a list.

list=[1,2,3,4,5,1,1,3,5]

duplicates = set()
uniques=[]

for i in list:
    if i not in duplicates:
        uniques.append(i)
        duplicates.add(i)

print(duplicates)