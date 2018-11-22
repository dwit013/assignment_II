list1 = []
n = int(input("Enter the number of elements in list"))
mul = int(input("Enter the number to multiply"))
for i in range(n):
    new_element = int(input("Enter a number"))
    list1.append(new_element)
print(f"The list is {list1}")
for i in range(n):
    list1[i] = list1[i] * mul

print(f"The list is {list1}")
