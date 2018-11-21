#Write a Python program to get a single string from two given strings, separated by a space and
#swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

string1=str(input("Enter first string: "))
string2=str(input("Enter second string: "))

s1=string2[:2]+string1[2:]
s2=string1[:2]+string2[2:]

print(s1," ",s2)
