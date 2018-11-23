#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return “Empty String”.

strn=input("Enter any string")
n=len(strn)
if n<2:
    print("Empty )
else:
    print(strn[0:2]+strn[n-2:n])