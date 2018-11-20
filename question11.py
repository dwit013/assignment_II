list1 = [(1,2,3),(5,4,2),(5,3,1)]
list3 = []
for i in list1:
    list2 = list(i)
    list2[len(i)-1] = 100
    t1 = tuple(list2)
    list3.append(t1)



print(list3)
