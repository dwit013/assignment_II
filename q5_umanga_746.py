list = []
count = 0

total = int(input("Enter total number of string you want to enter: "))

for i in range (0, total):
    string = input("Enter string: ")
    list.append(string)
print(list)
for i in list:
    if (len(i)>1 and i[:1].find(i[-1])):
        count = count + 1

print("Total stting with length 2 or more and whose first and last character are same = ", count)
