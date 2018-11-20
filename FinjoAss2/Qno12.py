'''

12. Write a Python program to remove an empty tuple(s) from a list of tuples.
Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

'''

data = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
list2=[]

for item in data:
    if item:
        list2.append(item)
        
print(list2)        
        
