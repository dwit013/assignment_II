list_random = []
n= int(input("Enter the number of elements in the list"))
if n > 7 :
    for i in range(n):
        new_element = input("Enter a element for the list :")
        list_random.append(new_element)

print(f"The list is {list_random}")
print(len(list_random))
del list_random[0]
del list_random[4]
del list_random[5]
print(f"The new list is {list_random}")


    
