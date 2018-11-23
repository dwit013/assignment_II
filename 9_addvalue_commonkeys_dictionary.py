Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d1 = {'a':10, 'b':20, 'c':30}
>>> d2 = {'a':40, 'c':50, 'd':20}
>>> for key,value in d1.items():
	if key in d2:
		d1[key] = value + d2[key]
		del d2[key]

		
>>> d1.update(d2)
>>> print(d1)
{'a': 50, 'd': 20, 'c': 80, 'b': 20}
>>> 
