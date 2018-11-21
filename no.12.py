12. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

tuple1=[(),(),('',),('a','b','c'),('a','b'),('d')]
tuple2=[]
for item in tuple1:
    print(item)
    if(item):
        tuple2.append(item)


print(tuple2)
