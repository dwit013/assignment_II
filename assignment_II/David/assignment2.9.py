from collections import Counter

d1={'a':300,'b':400,'c':676}
d2={'a':323,'c':989,'e':9898}

d=dict(Counter(d1)+Counter(d2))

print(d)

