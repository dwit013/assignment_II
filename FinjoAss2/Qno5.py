"""
Q no.5 )
Write a Python program to count the number of strings where the string length is 2 or more and
the first and last character are same from a given list of strings.
"""


list = []
count = 0

n = int(input("how many items in list: "))

for i in range(0,n):
    data = input("enter a string: ")
    list.append(data)

for item in list:
    l = len(item)
    if l >= 2:
        if item[0] == item[-1]:
            count=count+1
            
print(count)
