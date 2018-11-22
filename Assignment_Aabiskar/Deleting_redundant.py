list1 = []
n = int(input("Enter the number of elements in list :"))
for i in range(n):
    new_element = input("Enter an element:")
    list1.append(new_element)
print(f"The list is {list1}")
for i in range(n-1):
    for j in range(i+1,n):
        if list1[i] == list1[j]:
            del list1[j]
            n = len(list1)

print(f"The list is {list1}")
