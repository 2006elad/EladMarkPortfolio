string = input("Please enter a string: ")
string_1h = string[:len(string)//2]
string_2h = string[len(string)//2:]
string_1h = string_1h.lower()
string_2h = string_2h.upper()
string = string_1h + string_2h
print(string)
