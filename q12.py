#12.Write a Python program to remove an empty tuple(s) from a list of tuples.

l = [(),(),('',),('a','b'),('a','b','c'),('d')]

l = [t for t in l if t]
print(l)

