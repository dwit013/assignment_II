i=1
while i<=100:
    prime=True;
    j=2;
    while j<i:
        if i%j==0:
            prime=False;
            break;
        j+=1;
    if prime==True:
        print(f"{i} is a prime number.");
    i+=1;



