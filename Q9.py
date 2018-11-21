d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'c':400}
d3={}
print(d1)
print(d2)
for key1 in d1:
    for key2 in d2:
        if (key2==key1):
            d3[key2]=(d1[key2]+d2[key2]);

print(d3)




