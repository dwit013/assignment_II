#1.Write a program to print all prime numbers between 1 and 100
for i in range(2,101):
    for j in range(2,101):
        rem = i % j
        if(rem == 0):
            if(i == j):
                print(i,'is a prime number')
                break
            break

