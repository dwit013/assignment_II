print("Enter first word")
word1=input()
print("Enter second word")
word2=input()
w1=len(word1)
w2=len(word2)
if w1<2 or w2<2:
    print("Empty String");
    exit();

def exchange(a,b,loa):
            i=0;
            while i<loa:
                   if i<2:
                      print(b[i],end="");
                   else:
                      print(a[i],end="");

                   i+=1;

exchange(word1,word2,w1);
print(" ",end="");
exchange(word2,word1,w2);

