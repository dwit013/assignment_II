'''

9. Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

'''

from collections import Counter

dict1 = {'apple': 130, 'orange': 300, 'mango':300}
dict2 = {'apple': 250, 'orange': 150, 'banana':500}
someDict = Counter(dict1) + Counter(dict2)

print(someDict)
