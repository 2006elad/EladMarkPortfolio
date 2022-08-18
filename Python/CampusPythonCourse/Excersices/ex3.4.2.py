string = input("Please enter a string: ")
first_char = string[0]
string = string[1:]
string = string.replace(first_char, 'e', -1)
string = first_char + string
print(string)
