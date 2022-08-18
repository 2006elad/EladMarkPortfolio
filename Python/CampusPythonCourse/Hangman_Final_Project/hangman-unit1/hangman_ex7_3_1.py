def show_hidden_word(secret_word, old_letters_guessed):
    """
    Function that show the hidden words from old letter list that user guessed already.
    :param secret_word: The secret word he try to find
    :param old_letters_guessed: The list of word that user already used
    :type secret_word: str
    :type old_letters_guessed: list
    :return: The string of letters that player guess and they are found in secret word
    :rtype: str
    """
    secret_word_progress_list = ["_"] * len(secret_word)
    for i in range(0, len(old_letters_guessed)):
        if old_letters_guessed[i] in secret_word:
            for j in range(0, len(secret_word)):
                if old_letters_guessed[i] == secret_word[j]:
                    secret_word_progress_list[j] = secret_word[j]
    secret_word_progress_string = " ".join(secret_word_progress_list)
    return secret_word_progress_string


def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))


if __name__ == '__main__':
    main()