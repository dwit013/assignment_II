print("The prime numbers between 1 and 100 are :")
for i in range(0,100):
    count =0
    for j in range(1, i+1):
         if i % j ==0 :
            count = count + 1
    if count == 2:
         print(i)
    else:
        pass
