list = []

tot = int(input("Enter total element for list: "))

for i in range (0,tot):
    data = input("Enter data for list: ")
    list.append(data)

dup_items = set()
uniq_items = []
for x in list:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
