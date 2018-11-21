dict1 = {'A': 25, 'B': 41, 'C': 32}
dict2 = {'A': 21, 'B': 12, 'C': 62}
finaldict = {key:(dict1[key], dict2[key]) for key in dict1}
print(finaldict)
