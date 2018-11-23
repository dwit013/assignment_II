Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lis1 = [(10,20,40), (40,50,60), (70,80,90)]
>>> lis2 = []
>>> for i in lis1:
	t1 = list(i)
	t1[-1] = 30
	t2 = tuple(t1)
	lis2.append(tuple(t2))

	
>>> print(lis2)
[(10, 20, 30), (40, 50, 30), (70, 80, 30)]
>>> 
