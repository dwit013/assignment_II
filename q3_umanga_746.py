string = input("Enter two string seperated by space: ")

strings = string.split(" ")

part1 = strings[0][:2]

strings[0], strings[1] = strings[0].replace(strings[0][:2], strings[1][:2]), strings[1].replace(strings[1][:2], strings[0][:2])

print(strings[0] + " " + strings[1])
