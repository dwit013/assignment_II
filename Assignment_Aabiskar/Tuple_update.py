a = [(10,20,40),(40,50,60),(70,80,90)]
new_list=[]
num = int(input("Enter a number to replace in tuple"))
for i in a:
    tmp_list = list(i)
    tmp_list[-1] = num
    new_tuple = tuple(tmp_list)
    new_list.append(new_tuple)

print(new_list)
          
