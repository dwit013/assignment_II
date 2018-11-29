Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list=['abc','xyz','asa','5453']
>>> length=len(list)
>>> count=0
>>> for i in range(length):
	if(len(list[i])>=2 and list[i][0]==list[i][len(list[i])-1]):
		count=count+1

		
>>> print(count)
1
>>> 
