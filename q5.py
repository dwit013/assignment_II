#5.Write a Python program to count the number of strings where the string length is 2 or more and
# the first and last character are same from a given list of strings.

list =  ['abc', 'xyz', 'aba', '1221']
count = 0

for i in range(0,len(list)):
    string = list[i]
    if len(string) > 2:
        if string[0]==string[-1]:
            count = count + 1

print(count)

