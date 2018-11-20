list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

i = 0

string = input("Enter string to insert: ")

for x in list:
    list[i] = string + str(list[i])
    i = i+1;

print(list)
