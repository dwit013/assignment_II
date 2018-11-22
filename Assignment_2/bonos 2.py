# BONUS QUESTION

#Write a Python program to count the occurrences of each word in a given sentence.

#code

def count_word(str):
    counts = dict()
    words = str.split()

    for x in words:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1

    return counts

print( count_word('Ram is a boy. Ram is going to DWIT'))

