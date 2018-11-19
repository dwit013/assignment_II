#   Name: Abhishek Pandey
#   Roll no: 706

#5. Write a Python program to count the number of strings where the string length is 2 or 
#   more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221'] 
# Expected Result : 2

list=["abc","xyz","aba","1221"]
count=0
r= len(list)

for i in range(r):
    string=list[i]
    r2=len(string)
    if(len(string)>2):
        if(string[0]==string[r2-1] and string[1] == string[r2-2]):
            count= count+1

print(count)     