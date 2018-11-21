dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic = {}
for i in dic1.keys():
    print(i)
    dic[i] = dic1[i]

for i in dic2.keys():
    print(i)
    dic[i] = dic2[i]

for i in dic3.keys():
    print(i)
    dic[i] = dic3[i]
    
for i in dic.items():
    print(i)
