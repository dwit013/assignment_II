""" Write a Python program to count the number of strings where the string length is
2 or more and the first and last character are same from a given list of strings. 
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2 """

#code

def matching_words(string):
    count=0
    for words in string:
        if len(words)>1 and words[0] == words[-1]:
            count+=1

    return count

print(matching_words(['abc','xyz','aba','1221']))
