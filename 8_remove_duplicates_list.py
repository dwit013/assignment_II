Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = ['abc', 'abc', 1,2,6,8,2,3,1]
>>> new = []
>>> for i in range(0,len(l)):
	if l[i] not in new:
		new.append(l[i])

		
>>> print(new)
['abc', 1, 2, 6, 8, 3]
>>> 
