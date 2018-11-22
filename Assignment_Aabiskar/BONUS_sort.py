import operator
dict = {1:'Aabiskar',8: 'Sushil',4: 'Shubham',2: 'Janaki',5: 10,7: 1, 6: 11}
sort_dict = sorted(dict.items(), key=operator.itemgetter(0))
print(' Dictionary in ascending order as per the value: ',sort_dict)
sort_dict = sorted(dict.items(), key=operator.itemgetter(0),reverse=True)
print('Dictionary in decending order as per the value: ',sort_dict)
