lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

i=0

val = int(input("Enter number: "))

for x in lst:
    lst[i] = lst[i] * val
    i = i + 1

print(lst)
