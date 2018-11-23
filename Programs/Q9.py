#Write a Python program to combine two dictionary adding values for common keys.

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
counter={}

for key,x in d1.items():

    if key in d2:
        d1[key]=x+d2[key]
        del d2[key]

d1.update(d2)

print(d1)