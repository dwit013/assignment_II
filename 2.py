#   Name: Abhishek Pandey
#   Roll no: 706

# 2. Write a Python program to get a string made of the first 2 and the last 2 chars from a 
#    given a string. If the string length is less than 2, return “Empty String”.
# Sample String : ‘HelloworLD’ 
# Expected Result : 'HeLD' Sample String : 'a3' 
# Expected Result : 'a3a3' Sample String : 'w' 
# Expected Result : ‘Empty String’

print("Enter String: ")
string1 = input()

l = len(string1)

if(l<2):
    print("Empty String")

else:
    print("Result: ",string1[0],string1[1],string1[l-2],string1[l-1])