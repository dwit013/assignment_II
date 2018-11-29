Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> numbers = [1,2,3,4]
>>> s = 'emp'
>>> for i in range(0,len(numbers)):
	numbers[i] = s + str(numbers[i])

	
>>> numbers
['emp1', 'emp2', 'emp3', 'emp4']
>>> 
