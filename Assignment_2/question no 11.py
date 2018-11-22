""" Write a Python program to replace last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)] """

#code

list1 = [(10,20,40),(40,50,60),(70,80,90)]
list2 = []

for t in list1:
    t = t[:2] + (100,)
    list2.append(t)
    
print(list2)

    
    
