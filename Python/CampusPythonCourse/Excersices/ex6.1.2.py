def shift_left(my_list):
    """
    Get 3 length list and move each item to the next index
    :param my_list: list we moving
    :type my_list: list
    :return: new list after change
    :rtype: list
    """
    new_list = [0, 0, 0]
    new_list[0], new_list[1], new_list[2] = my_list[1], my_list[2], my_list[0]
    return new_list


print(shift_left(['monkey', 2.0, 1]))
