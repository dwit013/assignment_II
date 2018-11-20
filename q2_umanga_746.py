string = input("Enter String: ")
output = ''
strlen = len(string)
x=0;
y=0;


if(strlen<2):
    print('Empty String')
else:
    output = string[:2] + string[-2:]
    print (output)
