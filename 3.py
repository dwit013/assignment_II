#   Name: Abhishek Pandey
#   Roll no: 706

# 3. Write a Python program to get a single string from two given strings, 
#    separated by a space and swap the first two characters of each string. 
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xyc abz'

print("Enter String1: ")
string1=input()

print("Enter String2: ")
string2=input()

string1_up = string2[:2]+ string1[2:]

string2_up = string1[:2]+ string2[2:]

print("Combined string: ",string1_up,'',string2_up)

