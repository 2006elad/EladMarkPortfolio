def count_chars(my_str):
    """
    Function that make from string a dict with chars as string and the times each char is appear in the string as value
    :param my_str: The string we checking
    :type my_str: str
    :return: The dict with all values
    :rtype: dict
    """
    my_str = my_str.split()
    my_str = "".join(my_str)
    my_str_keys = set(my_str)
    my_str_dict = {}
    for key in my_str_keys:
        my_str_dict[key] = my_str.count(key)

    return my_str_dict


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))


if __name__ == '__main__':
    main()
