strn=input("Enter any string")
n=len(strn)
if n<2:
    print("Empty string")
else:
    print(strn[0:2]+strn[n-2:n])