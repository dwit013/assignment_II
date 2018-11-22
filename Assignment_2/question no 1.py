#Write a program to print all prime numbers between 1 and 100.

#code

flag=True
a = int(input("Enter the inital starting number: "))
b = int(input("Enter the last number upto which you want to find the prime number: "))

print("Prime number between",a,"and",b,"are as follows: ")

for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if(num % i) == 0:
                    flag=False
                    break
            if(flag):
                print(num)
            flag=True
            


