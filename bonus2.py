#  Write a Python program to count the occurrences of each word in a given sentence.

count = 0
print("Enter a sentence: ")
a=input()
a.lower

print("Enter the word: ")
b=input()
b.lower

for i in a:
    if (i==b):
        count=count+1 
    
print("Number of occurences: ",count)       