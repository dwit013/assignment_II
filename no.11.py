#Write a Python program to replace last value of tuples in a list.
#Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
#Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]


tuple = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("The tuple before replacement",tuple)
tuple1=[]
for new in tuple:
    new = new[:2]+(100,)
    tuple1.append(new)
     
print("The tuple after replacement",tuple1)
