def choose_word(file_path, index):
    """
    Hangman Function that read a file and return how much different word we have in file and what's the word
     in the index that player asked to get
    :param file_path: file dir
    :param index: The index of the word that player wants to get
    :type file_path: str
    :param index: int
    :return: A tuple first value is the number of the different word in file, and second is the word with the index
    :rtype: tuple
    """
    return_values = [0, 0]
    word_file_content = open(file_path, 'r+')
    word_file_content_list = word_file_content.readline().split()
    return_values[0] = len(set(word_file_content_list))
    count_iteration = 0
    i = 0
    while count_iteration <= index - 1:
        if count_iteration % len(word_file_content_list) == 0:
            i = 0
        if count_iteration == index - 1:
            return_values[1] = word_file_content_list[i]
        count_iteration += 1
        i += 1
    word_file_content.close()
    return tuple(return_values)


def main():
    print(choose_word(r"d:\words.txt", 3))
    print(choose_word(r"d:\words.txt", 15))


if __name__ == '__main__':
    main()