def longest(my_list):
    """
    Function that check in a list with string values who's is the longest
    :param my_list: list we check
    :type my_list: list
    :return: the string value in the list that it has the longest length
    :rtype: str
    """
    my_list.sort(key=len)
    return my_list[-1]


def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    print(longest(list1))


if __name__ == '__main__':
    main()