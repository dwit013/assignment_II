#Write a Python program to insert a given string at the beginning of all items in a list. 

a="emp"
b=[1,2,3,4]


intr=list(map(lambda x: a+str(x),b))

print(intr)