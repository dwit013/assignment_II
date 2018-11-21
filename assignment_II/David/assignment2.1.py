
for i in range(1,100):
    j=1
    c=0
    for j in range(1,100):
        if((i%j)==0):
            c=c+1


    if(c==2):
        print(i)

