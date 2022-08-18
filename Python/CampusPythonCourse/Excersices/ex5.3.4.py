def last_early(my_str):
    my_str = my_str.lower()
    last_letter = my_str[-1]
    my_str = my_str[:-1]
    if last_letter in my_str:
        return True
    else:
        return False


string = input("Please insert String: ")
print(last_early(string))
