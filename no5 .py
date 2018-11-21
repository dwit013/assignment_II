list=['abc', 'xyz', 'aba', '1221']
length=len(list)
count=0
for i in range(length):
    if(len(list[i])>=2 and list[i][0]==list[i][len(list[i])-1]):
        count=count+1

print(count)
