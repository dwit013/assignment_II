word = ['abcda','aba','12131','baanana']
j=0
k=0
for i in word:
    if len(i)>=2 and i[j]==i[len(i)-1]:
        k = k + 1


print(k)
