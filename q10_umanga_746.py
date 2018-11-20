d1 = {}
d2 = {}
d3 = {}
d_out = {}

tot1 = int(input("Enter total values for dictionary 1: "))
tot2 = int(input("Enter total values for dictionary 2: "))
tot3 = int(input("Enter total values for dictionary 3: "))


print("For dictionary 1:")

for i in range (0,tot1):
    key1 = int(input("Enter integer key: "))
    val1 = int(input("Enter integer value for the key: "))
    d1[key1] = val1

print("For dictionary 2:")

for i in range (0,tot2):
    key2 = int(input("Enter integer key: "))
    val2 = int(input("Enter integer value for the key: "))
    d2[key2] = val2

print("For dictionary 3:")

for i in range (0,tot3):
    key3 = int(input("Enter integer key: "))
    val3 = int(input("Enter integer value for the key: "))
    d3[key3] = val3

for key,val in d1.items():
    d_out[key] = val

for key,val in d2.items():
    d_out[key] = val

for key,val in d3.items():
    d_out[key] = val

print(d_out)
