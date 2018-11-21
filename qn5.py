
list=["aba","abc","1231"]
count=0

for val in list:
    n=len(val)
    if(n>=2 and(val[0]==val[n-1])):
        count=count+1

print("Expected result is ",count)
