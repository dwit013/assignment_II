# Q. NO: 1
flag = 0
for i in range(1, 101):
    if(i==1 or i==2):
        flag = flag+1
    for j in range(2,i):
        if( i%j == 0):
            flag = flag+1
    if(flag == 0):
        print(i)
    flag = 0


# Q. NO: 2
def  concat(string):
    if(len(string) < 2):
        return "EMPTY STRING"
    return (string[:2]+string[-2:])
string = input("Enter the String: ")
concat(string)



# Q. NO: 3
str1 = input("Enter the First String:")
str2 = input("Enter the Second String:")
if(len(str1) < 3 or len(str2) < 3):
    print("Please Enter strings with length greater than 2.")
    exit()
print( str2[:2] + str1[2:] + ' '+ str1[2:] + str2[2:] )


# Q. NO: 4
num = int(input("Enter the number: "))
mylist = [1, 2, 3, 4, "Hell", "Noobie", (2,3)]
mylist = [num*item for item in mylist]
print(mylist)


# Q. NO: 5
mylist = ["23132", "BOY", "1221", "bixtron", "aba"]
len1 = 0
for item in mylist:
    if(len(item) > 1 and item[0] == item[-1]):
        len1 = len1 + 1
print("The Length of the list with required condition is: ", len)


# Q. NO: 6
mylist = [123, "him", "12345", 2.987, (1,2,3), [1,2]]
if(len(mylist) < 5):
    print("Please Enter more items to your list")
    exit()
for j in [5, 4, 0]:
    mylist.pop(j)
print(newlist)



# Q. NO: 7
mylist = [1, 2, 3, 4, "Hell"]
init = "Emp"
i=0
for item in mylist:
    mylist[i] = init + str(item)
    i = i+1
print(mylist)


# Q. NO: 8
def dupRemove(mylist):
    temp = []
    for item in mylist:
        if item not in temp:
            temp.extend([item])
    return temp

mylist = [1,3,5,1,"hel", 5,3,"hel"]
print(dupRemove(mylist))


#Q. NO: 9
mydict1 = {"Harry":200, "Hermoine":405, "Ron":150, "Ginny":365}
mydict2 = {"Harry":200, "Luna":400, "Hermoine":405}
for item in mydict2.keys():
    if (item in mydict1.keys()):
        mydict1[item] = mydict1[item] +  mydict2[item]
    else:
        mydict1.update({item:mydict2[item]})

print(mydict1)


#Q. NO: 10
mydict1 = {45:200, "Hermoine":405, 56:150, "Ginny":365}
mydict2 = {200:200, "Luna":400, "Hello":405}
mydict3 = {1:4}
mydict1.update(mydict2)
mydict1.update(mydict3)
print(mydict1)


#Q. NO: 11
mylist1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
mylist2 = []
for item in mylist1:
    tuple1 = list(item)
    tuple1[-1] = 300
    tuple2 = tuple(tuple1)
    mylist2.append(tuple(tuple2))
print(mylist2)


#Q. NO: 12
mylist1 = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
mylist2 = []
for item in mylist1:
    if (item != ()):
        mylist2.append(item)
print(mylist2)
