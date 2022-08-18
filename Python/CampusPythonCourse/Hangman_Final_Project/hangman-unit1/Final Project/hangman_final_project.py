# Important ! - Please run this program in python interpreter(console) to get the best user experience
# Some features will not work on edit program like pyCharm etc...

import os
import time
import random

RANDOM_COLOR_LIST = ["\033[91m {}\033[00m", "\033[92m {}\033[00m", "\033[93m {}\033[00m", "\033[94m {}\033[00m",
                     "\033[95m {}\033[00m", "\033[96m {}\033[00m", "\033[97m {}\033[00m", "\033[98m {}\033[00m"]

HANGMAN_PHOTOS = {
    1: "x-------x\n\n\n\n",
    2: """
x-------x
|
|
|
|   
|
|\n\n""",
    3: """
x-------x
|       |
|       0
|
|
|
|\n\n""",
    4: """
x-------x
|       |
|       0
|       |
|
|\n\n""",
    5: """
x-------x
|       |
|       0
|      /|\\
|
|\n\n""",
    6: """
x-------x
|       |
|       0
|      /|\\
|      /
|\n\n""",
    7: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|\n\n"""}


def main():

    # Game words dir settings and welcome message
    start_game_print()
    words_file_dir = file_dir_validation()

    # -Game Start-
    is_game_finished = False
    while not is_game_finished:
        clear_console()
        index = index_validate()
        secret_word = choose_word(words_file_dir, index)
        clear_console()
        loading_print()
        clear_console()
        print("\n~~~~~~~~Game Started!~~~~~~~~\n")
        old_letter_guessed = []
        try_count = 1
        print_hangman(try_count)
        print('\n\n\n\n')
        game_secret_word_process_string = show_hidden_word(secret_word, old_letter_guessed)

        is_one_game_finished = False
        while not is_one_game_finished:  # Game loop until the game end with lose or win
            print("Secret word:", game_secret_word_process_string)
            is_letter_validated = False
            while not is_letter_validated:  # Loop that validate player has input validate letter
                guessed_letter = input("\n\nGuess a letter: ")
                if try_update_letter_guessed(guessed_letter, old_letter_guessed):
                    is_letter_validated = True
            # ~~~Letter is validated~~~

            # -Now checking Guessed letter and print the right message-

            # Check if player guesses right
            if show_hidden_word(secret_word, old_letter_guessed) == game_secret_word_process_string:  # Wrong answer
                try_count += 1
                time.sleep(1)
                clear_console()
                print("\nWrong! :(\n")
                time.sleep(1)
                print_hangman(try_count)
                time.sleep(1.5)
                if try_count == 7:
                    print(RANDOM_COLOR_LIST[0].format("~~~ You lose the game ~~~\n\n"))
                    print("~~~The secret word was:", end="")
                    print(RANDOM_COLOR_LIST[2].format(secret_word), '~~~\n\n')
                    is_one_game_finished = True

            else:  # Right answer
                time.sleep(1)
                clear_console()
                print("\nGreat! :)\n")
                time.sleep(1)
                print_hangman(try_count)
                time.sleep(1.5)
                game_secret_word_process_string = show_hidden_word(secret_word, old_letter_guessed)
                if check_win(secret_word, old_letter_guessed):
                    print(RANDOM_COLOR_LIST[1].format("~~~ You won the game ~~~\n\n"))
                    is_one_game_finished = True
            # ~~~ One game Finished ~~~

        # -Check if player want to play another game or quit-

        if end_game_choice_validation():   # Don't want to play another game
            is_game_finished = True
            clear_console()
            time.sleep(1)
            print("~~~~ Bye bye ~~~~\n\n~~~~ Thank you for playing with us ~~~~")
            time.sleep(2)
        else:   # Want to play another game
            clear_console()
            print("~~~Initializing game~~~")
            time.sleep(1.5)
            clear_console()


def start_game_print():
    """
    Function that print the start of the welcome to the game message
    :return: None
    """
    print("Welcome to the game Hangman")
    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/\n\n\n""")


def file_dir_validation():
    """
    Function that validate the directory of the words file is exist.
    if not exist user inputs again until the file is found
    :return: The validate dir
    :rtype: str
    """
    word_file_dir = None
    is_dir_validated = False
    while not is_dir_validated:
        word_file_dir = input("Please put words file directory: ")
        loading_print()
        if not os.path.isfile(word_file_dir):   # Check if file found in the computer
            print("\n\nFile didn't exist please check file or insert the dir again!\n\n")
        else:
            is_dir_validated = True
    return word_file_dir


def loading_print():
    """
    Function that print loading affect with sleep timer
    :return: None
    """
    from time import sleep
    loading = 'LOADING...'
    for i in range(10):
        print(loading[i], sep=' ', end=' ', flush=True)
        sleep(0.5)
    print('\n\n')


def index_validate():
    """
    Function that input index number from player and validate that it is a number and positive
    :return: The validated index number
    :rtype: int
    """
    index = None
    is_valid = False
    while not is_valid:
        try:
            index = int(input("\nPlease input the index(positive and bigger than 1) of the word you want to guess: "))
        except ValueError:
            loading_print()
            print("You can enter only numbers, please try again! ")
        else:
            loading_print()
            if index <= 0:
                print("You can enter only natural number(positive numbers and bigger than 1),\nPlease try again!\n")
            else:
                is_valid = True
    return index


def clear_console():
    """
    Function that clear print console (Can view only in the interpreter)
    :return: None
    """
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def print_hangman(num_of_tries):
    """
    Function that print the hangman arts by player num of guesses
    :param num_of_tries: The player num go guesses
    :return: None
    """
    random_color_choice = random.choice(RANDOM_COLOR_LIST)
    print(random_color_choice.format(HANGMAN_PHOTOS[num_of_tries]))


def choose_word(file_path, index):
    """
   Function that read the words file and return the secret word by the index user inputted
    (If index is bigger than word in file, the index return back to zero everytime until the word is find)
    :param file_path: file dir
    :param index: The index of the word that player wants to get
    :type file_path: str
    :param index: int
    :return: The secret word
    :rtype: str
    """
    # Important Note - i change the original function(that return a tuple)
    # and remove this line that calculate how much difference words we have in the file.
    # As the recommendation it is useless to calculate this in the real game.
    # So i returned only the secret word.

    secret_word = ""
    word_file_content = open(file_path, 'r+')
    word_file_content_list = word_file_content.readline().split()
    count_iteration = 0
    i = 0
    while count_iteration <= index - 1:   # Loop until the iteration counter is equal to index
        if count_iteration % len(word_file_content_list) == 0:  # Reset i after we finish to pass all of the words
            i = 0
        if count_iteration == index - 1:    # Check if the word is found
            secret_word = word_file_content_list[i]
        count_iteration += 1
        i += 1

    word_file_content.close()
    return secret_word


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


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Function that print message when letter have been used before or not validated by rules,
    otherwise - add it to guessed letter list
    :param letter_guessed: letter string that been inputted by user
    :param old_letters_guessed: old letters that already been used by player
    :return: True when the play word is validated, otherwise - return false and print message
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):  # letter validated
        old_letters_guessed.append(letter_guessed.lower())
        return True

    else:   # Word didn't validated
        if letter_guessed in old_letters_guessed:   # Check if the reason is that the letter already been used
            print(" -> ".join(sorted(old_letters_guessed)), '\n\nPlease insert another letter!\n')
        return False


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
    if len(letter_guessed) > 1:
        print("X\nThe string is to long, please try again! ")
        return False

    elif not letter_guessed.isalpha():
        print("X\nYou can enter only alphabetic letters")
        return False

    elif letter_guessed in old_letters_guessed:
        print("X\n")
        time.sleep(1)
        print("You already guessed this letter!\n\nThis is letters list you already guessed:")
        return False

    else:   # Word validated
        return True


def check_win(secret_word, old_letters_guessed):
    """
    Function that check if player win the game by guessing all of the right words.
    :param secret_word: String of the secret word that player need to guess
    :param old_letters_guessed: list that include the word that player already guessed
    :type secret_word: str
    :type old_letters_guessed: list
    :return: True if player win and finish the game, else False - if player have more letters to find.
    """
    player_progress_list = (show_hidden_word(secret_word, old_letters_guessed)).split()
    if secret_word == "".join(player_progress_list):
        return True
    else:
        return False


def end_game_choice_validation():
    """
    Function get from user a choice if he want to end and exit the game or continue to another game.
    The function also valid user input - that choice input is: 'Y' OR 'N'
    :return: True - Want to finish the game, else False - Want to player another game:
    :rtype: bool
    """
    choice = ""
    choice_validated = False
    while not choice_validated:
        choice = input("Do you want to player another game?\nInput Y/N: ")

        if len(choice) != 1 or not choice.isalpha():
            print("\nYou enter invalid choice.\nTry Again!\n")

        elif choice.upper() == 'Y' or choice.upper() == 'N':
            choice_validated = True

        else:   # If user input another alphabetic letter that aren't 'N' OR 'Y'
            print("\nYou enter invalid choice.\nTry Again!\n")

    if choice.upper() == 'N':
        return True
    else:
        return False


if __name__ == '__main__':
    main()
