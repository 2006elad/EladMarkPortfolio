def is_funny(string):
    """
    Function that return True if string is included only 'h' and 'a'
    :param string: The string we check
    :return: True if yes, else False
    :rtype: bool
    """
    return False not in [False if char != 'h' and char != 'a' else True for char in string]


def main():
    print(is_funny("hahahahahaha"))
    print(is_funny("hahaxhahahaha"))


if __name__ == '__main__':
    main()
