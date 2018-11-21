dict1 ={
    'a' : 100,
    'b' : 230,
    'c' : 500
}
dict2 = {
    'a' : 200,
    'b' : 600,
    'd' : 300
}

for key, value in dict1.items():
    if key in dict2:
        dict1[key] = value + dict2[key]
        del dict2[key]

dict1.update(dict2)

print(dict1)


