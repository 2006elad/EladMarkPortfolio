from hangman_ex6_4_1 import check_valid_input as valid_letter_func


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Function that print message when letter have been used before or not validated by rules,
    otherwise - add it to guessed letter list
    :param letter_guessed: letter string that been inputted by user
    :param old_letters_guessed: old letters that already been used by player
    :return: True when the play word is validated, otherwise - return false and print message
    :rtype: bool
    """
    if valid_letter_func(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


def main():
    old_letters = ['a', 'p', 'c', 'f']
    print(try_update_letter_guessed('A', old_letters))
    print(try_update_letter_guessed('s', old_letters))
    print(old_letters)
    print(try_update_letter_guessed('$', old_letters))
    print(try_update_letter_guessed('d', old_letters))
    print(old_letters)


if __name__ == '__main__':
    main()
