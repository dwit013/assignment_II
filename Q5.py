list= ['abc', 'xyz', 'aba', '1221']
counter=0
for item in list:
    if len(item)>2 and item[0]==item[len(item)-1]:
        counter+=1;

print(f"There are {counter} such words.")
