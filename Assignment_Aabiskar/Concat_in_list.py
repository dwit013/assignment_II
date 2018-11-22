list1 = []
n = int(input("Enter the number of elements in list :"))
concat = input("Enter the string to concatenate :")
for i in range(n):
    new_element = input("Enter an element:")
    list1.append(new_element)
print(f"The list is {list1}")
for i in range(n):
    list1[i] = concat + list1[i] 

print(f"The list is {list1}")
