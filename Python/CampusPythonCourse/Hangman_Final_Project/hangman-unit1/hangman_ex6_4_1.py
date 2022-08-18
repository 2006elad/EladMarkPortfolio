def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Function check if the letter that been inputted by user is valid
    :param letter_guessed: the guessed letter string we want to valid
    :type letter_guessed: str
    :param old_letters_guessed: list of all the letter that already been guessed by the play
    :type old_letters_guessed: list
    :return: True if it is validated, else - false
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if len(letter_guessed) > 1 or not letter_guessed.isalpha():
        return False
    else:
        if letter_guessed not in old_letters_guessed:
            return True
        else:
            return False


def main():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))
    print(check_valid_input('ep', old_letters))
    print(check_valid_input('$', old_letters))
    print(check_valid_input('s', old_letters))


if __name__ == '__main__':
    main()