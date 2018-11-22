d1 = {'a' : 100, 'b':200, 'c':300, 'd' : 100, 'e' : 10}
d2 = {'a': 300, 'b':200, 'd' : 400, 'f' : 20, 'c':10}
d3 = {}

for key1 in d1:
    for key2 in d2:
        if key1 == key2 :
            d3[key1] = d1[key1] + d2[key2]
            break
        else:
            d3[key1] = d1[key1]
            d3[key2] = d2[key2]
print(d3)
