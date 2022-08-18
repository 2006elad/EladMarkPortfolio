def mult_tuple(tuple1, tuple2):
    """
    Function that create from numbers in two tuples - one tuple that include all pairs we can create
     (pairs are in tuples)
    :param tuple1: first numbers tuple
    :param tuple2: second numbers tuple
    :type tuple1: tuple
    :type tuple2: tuple
    :return: All pair tuple
    :rtype: tuple
    """
    pairs_tuple = []
    for num_from_tuple1 in tuple1:
        for num_from_tuple2 in tuple2:
            if num_from_tuple1 != num_from_tuple2:
                pair1 = (num_from_tuple1, num_from_tuple2)
                pair2 = (num_from_tuple2, num_from_tuple1)
                if pair1 not in pairs_tuple:
                    pairs_tuple.append(pair1)
                if pair2 not in pairs_tuple:
                    pairs_tuple.append(pair2)
            else:
                same_num_pair = (num_from_tuple1, num_from_tuple1)
                if same_num_pair not in pairs_tuple:
                    pairs_tuple.append(same_num_pair)
    return tuple(pairs_tuple)


def main():
    first_tuple = (1,4, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

    first_tuple = (1, 2, 3)
    second_tuple = (4, 5, 2, 6, 1)
    print(mult_tuple(first_tuple, second_tuple))


if __name__ == '__main__':
    main()