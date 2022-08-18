def are_lists_equal(list1, list2):
    """
    Function check if two list have same values, although they have different order
    :param list1: list number 1 we check
    :param list2: list number 2 we check
    :type list1: list
    :type list2: list
    :return: True if the equal, else False
    :rtype: bool
    """
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    print(are_lists_equal(list1, list2))
    print(are_lists_equal(list1, list3))


if __name__ == "__main__":
    main()