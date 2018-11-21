# 8.Write a Python program to remove duplicates from a list

l = [1,2,3,2,4,5,6,4]
non_duplicate = []

for i in range(0,len(l)):
    if i not in non_duplicate:
        non_duplicate.append(i)

print(non_duplicate)
