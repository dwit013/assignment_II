from collections import Counter

sentence = raw_input("Enter sentence:")

lst = sentence.split()

print(Counter(lst))
