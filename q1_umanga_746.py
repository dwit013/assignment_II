prime = True;

print("List of Prime Numbers between 1 and 100:")

for i in range (1,100, 1):
    for j in range (2, int(i/2), 1):
        if i % j == 0:
            prime = False
            break;
    if (i<2):
        prime = False;
    if(prime):
        print (i)
    prime = True
