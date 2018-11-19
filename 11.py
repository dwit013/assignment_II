#   Name: Abhishek Pandey
#   Roll no: 706

# 11. Write a Python program to replace last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

initial = [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 

tuple2 = []
for i in initial: 
    t = list(i) 
    t[-1]=100 
    z = tuple(t) 
    tuple2.append(tuple(z))

print (tuple2)