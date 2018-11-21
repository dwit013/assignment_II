#10.Write a Python script to concatenate dictionaries and create a new one

d1 = {1:2,2:3}
d2 = {3:4,4:5}
d3 = {5:6,7:8}

d1.update(d2)
d1.update(d3)
print(d1)
