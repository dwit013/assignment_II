#Write a program to print all prime numbers between 1 and 100

for num in range(1,101):
    temp = 0
    if num < 2:
        temp=1
    else:
        for i in range(2,num):
            if num % i == 0:
                temp=1
    if(temp==0):            
        print(num) 
