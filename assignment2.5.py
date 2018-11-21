l1=['aabc','xuzz','1234','aabd','aaba']
c=0
a=0
for i in l1:
    a=a+1
    if(len(i)>2):
        for j in l1[a:]:
            if(i[0]==j[0]):
                c=c+1
print(c)









