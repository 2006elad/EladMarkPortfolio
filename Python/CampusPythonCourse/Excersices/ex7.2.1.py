def is_greater(my_list, n):
    """
    Function create new list with numbers in the list we get that  greater than n
    :param my_list: the number list we checking
    :param n: the number we checking
    :type my_list: list
    :type n: int
    :return: new list the numbers that greater than n
    :rtype: list
    """
    new_list = []
    for current_number in my_list:
        if current_number > n:
            new_list.append(current_number)
    return new_list


def main():
    result = is_greater([1, 30, 25, 60, 27, 28], 28)
    print(result)


if __name__ == '__main__':
    main()
