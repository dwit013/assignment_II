""" Write a Python script to concatenate dictionaries and create a new one. 
Sample Dictionary : dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """

#code


dic1 = {1:10,2:20}
dic2 = {3:30,4:40}
dic3 = {5:50,6:30}

dic4 = {}

for key,val in dic1.items():
    dic4[key] = val

for key,val in dic2.items():
    dic4[key] = val

for key,val in dic3.items():
    dic4[key] = val

print(dic4)

