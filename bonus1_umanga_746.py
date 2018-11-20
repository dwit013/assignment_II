import operator

dic1 = {}

tot = int(input("Enter total values for dictionary: "))

for i in (0,tot):
    key = raw_input("Enter key: ")
    value = raw_input("Enate value for key: ")
    dic1[key] = value

dic2 = sorted(dic1.items(), key=operator.itemgetter(1))

dic3 = sorted(dic1.items(), key = operator.itemgetter(1), reverse = True)

print("Sorted by value in Ascending order:")
print(dic2)

print("Sorted by value in Descending order:")
print(dic3)
