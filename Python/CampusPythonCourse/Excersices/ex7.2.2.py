def numbers_letters_count(my_str):
    """
    Function that count in string digits and non-digit characters and return them in list
    :param my_str: the string we check
    :type my_str: list
    :return: list that in 0 index = digit characters, 1 index non digits characters
    """
    count_list = [0, 0]
    for char in my_str:
        if char.isdigit():
            count_list[0] += 1
        else:
            count_list[1] += 1

    return count_list


def main():
    print(numbers_letters_count("Python 3.6.3"))


if __name__ == '__main__':
    main()