d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
print(d1.keys())
for i in d1.keys():
    for j in d2.keys():
        if(i==j):
            print(d1.update(i+j))
