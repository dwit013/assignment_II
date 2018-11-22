def count_word(str1):
    counts = dict()
    for x in str1:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

    
 count = count_word('Ram is a boy. Ram is going to DWIT')
 print(count)

