#11. Write a Python program to replace last value of tuples in a list.

l1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
l2 = []
for item in l1:
    t1 = list(item)
    t1[-1] = 400
    t2 = tuple(t1)
    l2.append(tuple(t2))
print(l2)
