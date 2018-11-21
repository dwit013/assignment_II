str1=input("Enter your first string:")

if len(str1)<2:
    print("Your string is not long enough")
else:
    cs1=str1[0:2]
    cs2=str1[-2:]
    final=cs1+cs2
    print(final)
