'''

11. Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

'''
newTup = []
tup = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

for item in tup:
    item = item[:2]+(100,)
    newTup.append(item)

    

print(newTup)
