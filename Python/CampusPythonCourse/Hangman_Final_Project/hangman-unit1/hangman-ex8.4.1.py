HANGMAN_PHOTOS = {
    1: "x-------x",
    2: """
x-------x
|
|
|
|   
|
|""",
    3: """
x-------x
|       |
|       0
|
|
|
|""",
    4: """
x-------x
|       |
|       0
|       |
|
|""",
    5: """
x-------x
|       |
|       0
|      /|\\
|
|""",
    6: """
x-------x
|       |
|       0
|      /|\\
|      /
|""",
    7: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}


def print_hangman(num_of_tries):
    """
    Function that print the hangman arts by player guesses
    :param num_of_tries: The player num go guesses
    :return: None
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def main():
    num_of_tries = 7
    print_hangman(num_of_tries)


if __name__ == '__main__':
    main()
