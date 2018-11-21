#3.Write a Python program to get a single string from two given strings, separated by a space and
# swap the first two characters of each string.

str1 = 'apple'
str2 = 'ball'

str2[0]+str1[1:]+' '+str1[0]+str2[1:]
