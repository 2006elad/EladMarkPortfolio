def is_valid_input(letter_guessed):
    """
    Function check if the letter that been inputted by user is valid
    :param letter_guessed: the guessed letter string we want to valid
    :type letter_guessed: str
    :return: True if it is validated, else - false
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    else:
        return True


print(is_valid_input("app$"))
