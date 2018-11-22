""" Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd'] """

#code

list1 = [(),(),("",),('a','b'),('a','b','c'),('d')]
list2 = []

for i in list1:
    if(i):
        list2.append(i)

print(list2)
