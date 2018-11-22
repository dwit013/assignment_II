list_str = []
count = 0
n = int(input("Enter the number of strings in list"))
for i in range(n):
    new_str = input("Enter a string")
    if len(new_str) > 2 :
        list_str.append(new_str)
    else:
        print("Enter string with length greater than 2")
        pass

print(f"List is {list_str}")
for i in list_str:
    if i[0] == i[-1]:
        count = count + 1

print(f"Number of strings with same 1st and last character : {count}")
