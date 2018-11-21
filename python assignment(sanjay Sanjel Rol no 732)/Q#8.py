mylist=["a","sad","damn","hello","yes","hello",2,3,4,56,4,32,43,32,54,"sad"]
newlist=[]
for i in mylist:
    if i not in newlist:
        newlist.append(i)
print(newlist)
