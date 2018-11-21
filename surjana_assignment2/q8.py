def removed(li):
 new_li = []
 for elem in li:
    if elem not in new_li:
        new_li.append(elem)
 return new_li

li = [1,2,5,4,7,8,1,4,5,2]
print(li)
print(removed(li))
