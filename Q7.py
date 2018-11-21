print("Enter a word")
word=input()
list= [1,2,3,4]
i=0
for item in list:
    list[i]=[f"{word}{item}"];
    i+=1;
print(list)

