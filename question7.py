value = [1,2,3,4,5,6]
string = input("Enter string to write at begining:")
newList = []
for i in value:
    newList.append(string + str(i))

print(newList)
