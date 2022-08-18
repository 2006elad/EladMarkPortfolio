def intersection(list_1, list_2):
    """
    Function that put all the intersection values in list
    :param list_1: numbers list 1
    :param list_2: numbers list 2
    :return: list of intersection numbers
    :rtype": list
    """
    return list(set([x for x in list_1 for y in list_2 if x == y]))


def main():
    print(intersection([1, 2, 3, 4], [8, 3, 9]))
    print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))


if __name__ == '__main__':
    main()