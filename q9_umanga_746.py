d1 = dict()
d2 = dict()

tot1 = int(input("Enter total number of values for first dictionary: "))
tot2 = int(input("Enter total number of values for second dictionary: "))

print("For dictionary 1:")

for i in range (0,tot1):
    key1 = raw_input("Enter key: ")
    val1 = int(input("Enter integer value for the key: "))
    d1[key1] = val1

print("For dictionary 2:")

for i in range (0,tot2):
    key2 = raw_input("Enter key: ")
    val2 = int(input("Enter integer value for the key: "))
    d2[key2] = val2

for key,val in d1.items():
    if (key in d2):
        d2[key] = val + d2[key]
    else:
        d2[key] = val

print(d2)
    
