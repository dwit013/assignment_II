from collections import Counter
dict1={'a':500,'b':200}
dict2={'a':500,'b':300}
finaldict=Counter(dict1)+Counter(dict2)
print(finaldict)
