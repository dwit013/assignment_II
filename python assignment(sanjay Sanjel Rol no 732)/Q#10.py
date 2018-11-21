def Merge(dict1,dict2):
    result = {**dict1,**dict2}
    return result


dict1={'1':200,'2':500,'3':500,'4':1000}
dict2={'5':211,'6':700,'7':900,'8':250}
dict3=Merge(dict1,dict2)
print(dict3)
