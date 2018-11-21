#Write a Python script to concatenate dictionaries and create a new one.
#Sample Dictionary :
#dic1 = {1:10, 2:20}
#dic2 = {3:30, 4:40}
#dic3 = {5:50, 6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dict1 = {'a':10, 'b':20}
dict2 = {'x':30, 'y':40}
dict3 = {'p':50, 'q':60}

dict4={**dict1,**dict2,**dict3}

print(dict4)
