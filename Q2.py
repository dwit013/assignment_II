print("Enter a word")
word=input()
l=len(word)
if l<2:
    print("Empty String");
    exit();
print(f"{word[0]}{word[1]}{word[l-2]}{word[l-1]}")
