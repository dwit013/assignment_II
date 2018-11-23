

#Write a program to print all prime numbers between 1 and 100

for i in range(1,101):
    flag = 0
    if num < 2:
        flag=1
    else:
        for i in range(2,num):
            if num % i == 0:
                flag=1
    if(flag==0):            
        print(num) 
