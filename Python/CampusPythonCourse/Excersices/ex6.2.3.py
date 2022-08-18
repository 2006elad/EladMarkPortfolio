def format_list(my_list):
    """
    The function gets even list and return list with only even indexes values and the last values with and
    :param my_list: the list we using
    :type my_list: list
    :return: the new String
    :rtype: String
    """
    new_list = my_list[::2]
    string = " ".join(new_list) + " and " + my_list[-1]
    return string


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
print(format_list(my_list))
