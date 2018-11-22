#BONUS QUESTION
#Write a Python script to sort (ascending and descending) a dictionary by value.

#code

import operator

dict = {1:'Ramesh',4: 'Rohan',3: 'Rajesh',2: 'Janaki',5: 1,7: 10, 6: 11}

sort_dict = sorted(dict.items(), key=operator.itemgetter(0))

print(' Dictionary in ascending order as per the value: ',sort_dict)

sort_dict = sorted(dict.items(), key=operator.itemgetter(0),reverse=True)

print('Dictionary in decending order as per the value: ',sort_dict)
