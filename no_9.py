#Write a Python program to combine two dictionary adding values for common keys. 
#d1 = {'a': 100, 'b': 200, 'c':300}
#d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict1={'a':100,'b':200,'c':300}
dict2={'a':300,'b':200,'d':400}

result = {key: dict1.get(key, 0) + dict2.get(key, 0)
for key in set(dict1) | set(dict2)}
print(result)
