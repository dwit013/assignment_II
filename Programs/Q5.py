#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

a=['abc','xyz','aba','1221']
c=0
i=0

for i in range(1,len(a)):
    if len(a[i]) > 2 and a[i][0] == a[i][-1]:
        c = c + 1

print(c)




