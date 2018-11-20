tuple1 = (0, 1, 2, 3)
tuple2 = (4, 5, 6, 7)
tuple3 = (8, 9, 10, 11)
tuple4 = [tuple1, tuple2, tuple3]


print("Before:")
print(tuple4)

x=0;

for i in tuple4:
    lst = list(i)
    lst[-1] = 100
    lst = tuple(lst)
    tuple4[x] = lst
    x = x + 1
print("After:")
print(tuple4)
