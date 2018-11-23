#Write a Python program to remove an empty tuple(s) from a list of tuples.
#Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
 
tuple= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print("Tuple Before",tuple)
tuple1=[]
for new in tuple:
    if new:
        tuple1.append(new)
        
print("Tuple after",tuple1)
