Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = ['abc','1221','123','aba','aa']
>>> count = 0
>>> for i in range(0,len(l)):
	if(len(l[i])>2):
		if(l[i][0] == l[i][-1]):
			count += 1

			
>>> print (count)
2
>>> 
