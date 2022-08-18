# main function that gets string and k and return the right string by the rules
def str_opt(string, k):
    if k % 2 == 0:  # if the k is even

        if k >= 0:  # if the k is even and positive
            string = string.replace(' ', '#')  # Replace spaces with #

        else:  # if k is even and negative
            string_list = string.split(' ')  # split the string to list of words
            string = ""
            # because we using item for loop we add index number for each item
            string_list = list(enumerate(string_list))
            # loop that run through the string list and create a string that contain word that without E or e in them
            for index, word in string_list:
                if 'E' not in word and 'e' not in word:
                    if index != len(string_list) - 1:  # if we are in the sentence we aren't adding useless space
                        string = string + word + " "
                    else:
                        string = string + word

    else:  # if k is odd
        if k >= 0:  # if k is odd and positive
            string = string.lower()
            string_list = string.split(' ')
            string = ""
            string_list = list(enumerate(string_list))
            # loop that run through the string list and create new string with the original word with upper first letter
            for index, word in string_list:
                first_letter = word[0].upper()
                word = word[1:]
                if index != len(string_list) - 1:  # if we are in the sentence we aren't adding useless space
                    string = string + first_letter + word + " "
                else:
                    string = string + first_letter + word

        else:  # k is odd and negative
            string = string[::-1]  # Reverse the string

    return string


def string_validation(string):  # sub main function that validate the string input is contain only letters or spaces
    for ch in string:
        if not ch.isalpha() and ch != ' ':
            return False
    return True


# Main function
global k
print("Please insert String:")
string = input()
string_is_valid = False
while not string_is_valid:  # while loop that run until the string input by user is validate
    if not string_validation(string):
        print("The string can only contain letters and spaces!\nPlease try again!")
        string = input()
    else:
        string_is_valid = True

print("Please insert k value:")
k_is_valid = False
while not k_is_valid:   # loop that run until the user is input k that contain only integers
    try:
        k = int(input())
    except ValueError:
        print("You can enter only Integers\nPlease try again:")
    else:
        k_is_valid = True

print("The final string with the values you entered is:\n" + str_opt(string, k))    # print the final string
