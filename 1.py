#   Name: Abhishek Pandey
#   Roll no: 706

#1. Write a program to print all prime numbers between 1 and 100.
for n in range(1,101):
    flag = 1
    if n < 2:
        flag=0
    else:
        for i in range(2,n):
            if n % i == 0:
                flag=0
    if(flag==1):            
        print(n, '', sep=',', end='')