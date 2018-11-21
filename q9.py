#9. Write a Python program to combine two dictionary adding values for common keys.

from collections import counter
d1 = {'a':5, 'b':10, 'c':15}
d2 = {'a':5, 'b':50, 'd':2}

for key, value in d1.items():
    if key in d2:
        d1[key] = value + d2[key]
        del d2[key]
d1.update(d2)
print(d1)
