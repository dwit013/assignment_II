
for x in range(2, 100):
    flag = 1
    for y in range(2, x - 1):
        if (x % y == 0):
            flag = 0
            break
    if (flag != 0):
        print(x)
