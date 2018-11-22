#Write a Python program to multiply each item in a list by an integer

list = [1,2,3,10]
print("The list is", list)
num = int(input("Enter the integer to multiply: "))
for i in list:
    print(i * num)
