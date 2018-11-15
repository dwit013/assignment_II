#   Name: Abhishek Pandey
#   Roll no: 706

# 4. Write a Python program to multiply each item in a list by an integer.

print("Enter integr to multiply: ")
num1 = int(input())

list=[1,2,3,45,6,7]

r = len(list)

for i in range(r):
    list[i]=list[i]*num1
print(list)    