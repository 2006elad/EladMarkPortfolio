def inverse_dict(my_dict):
    """
    Function that reverse the dictionary by replace the key to be the value and value to be the key,
     same values that we replace them to be the keys will be in a list.
    :param my_dict: The dictionary we inverse
    :type my_dict: dict
    :return: The inverse dict
    :rtype: dict
    """
    inverse_dict_keys = set(my_dict.values())
    new_inverse_dict = {}
    for inverse_dict_key in inverse_dict_keys:
        if list(my_dict.values()).count(inverse_dict_key) >= 2:
            new_inverse_dict[inverse_dict_key] = get_list_on_same_values(my_dict, inverse_dict_key)
        else:
            new_inverse_dict[inverse_dict_key] = get_inverse_value(my_dict, inverse_dict_key)

    return new_inverse_dict


def get_list_on_same_values(my_dict, the_inverse_dict_key_we_want_to_found):
    """
    sub function that return a list of keys that have the same value. in our case this list in the inverse value dict
    :param my_dict: The dict we checking
    :param the_inverse_dict_key_we_want_to_found: The value that inverse to be the key in the inverse dict
    :return: a list of all of the keys that have the value we want to find
    :rtype: list
    """
    value_list = []
    for inverse_dict_value, inverse_dict_key in my_dict.items():
        if the_inverse_dict_key_we_want_to_found == inverse_dict_key:
            value_list.append(inverse_dict_value)
    value_list.sort()
    return value_list


def get_inverse_value(my_dict, inverse_dict_key):
    """
    sub function that return the key on a specific value, only relevant in our case when we know there is only one key
     with that value in the dict. this relevant to get the inverse value for the inverse func.
    :param my_dict: The dict we are checking
    :type my_dict: dict
    :param inverse_dict_key: The value we want to find and return his key
    :return: the inverse value
    """
    for key, value in my_dict.items():
        if value == inverse_dict_key:
            return key


def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))


if __name__ == '__main__':
    main()