list=["Sam","Alone","Nishad","Subham","Aayu","Aayu","Sam"]
print(list)
i=0
j=0

while i<(len(list)):
    if (list[1]==list[i]):
        del(list[i]);
    i+=1;

print(list)
