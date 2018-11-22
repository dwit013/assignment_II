""" Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string. 
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz' """


#code

string = input("Enter the string: ")
x , y = string.split(" ")

x , y =x.replace(x[:2],y[:2]) , y.replace(y[:2],x[:2])

print(x+" "+y)

