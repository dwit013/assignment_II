#   Name: Abhishek Pandey
#   Roll no: 706

# 9. Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300} 
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

d1 = {'x': 800, 'a': 200, 'd':300} 
d2 = {'x': 300, 'b': 200, 'd':400}

for key, value in d1.items():
    if key in d2:
        d1[key] = value + d2[key]
        del d2[key]
        d3={**d1,**d2}

print(d3)
