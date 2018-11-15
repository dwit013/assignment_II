#   Name: Abhishek Pandey
#   Roll no: 706

# 11. Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 

list2 = [t[:-1] + (100,) for t in list]

print(list2)