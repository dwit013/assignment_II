#7. Write a Python program to insert a given string at the beginning of all items in a list.

l = [1,2,3,4]
s = 'emp'

for i in range(0,len(l)):
    l[i] = s+str(l[i])

print(l)
