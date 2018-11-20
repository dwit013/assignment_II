tot=0
list = []

while(tot<6):
    tot = int(input("Enter total items in list: "))

for i in range(0,tot):
    val = input("Enter item for list: ")
    list.append(val)

i=0;

for x in list:
    if(i == 0 or i == 4 or i == 5):
        list.remove(x)
    i = i+1

print(list)
