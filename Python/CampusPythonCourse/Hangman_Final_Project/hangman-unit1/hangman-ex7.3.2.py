from hangman_ex7_3_1 import show_hidden_word


def check_win(secret_word, old_letters_guessed):
    """
    Function that player is win
    :param secret_word: String of the secret word that player need to guess
    :param old_letters_guessed: list that include the word that player already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if player win, else False
    """
    player_progress_list = (show_hidden_word(secret_word, old_letters_guessed)).split()
    if secret_word == "".join(player_progress_list):
        return True
    else:
        return False


def main():
    secret_word = "friends"
    old_letters_guessed = ['m', 'p', 'j', 'i', 's', 'k']
    print(check_win(secret_word, old_letters_guessed))

    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()