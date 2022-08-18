def squared_numbers(start, stop):
    """
    Function that print the power of the values between start par and include stop value
    :param start: start value
    :param stop: stop value
    :type start: int
    :type stop: int
    :return: list with each iterate value in power
    :rtype: list
    """
    new_list = []
    while start <= stop:
        new_list.append(start ** 2)
        start += 1
    return new_list


def main():
    print(squared_numbers(4, 8))
    print(squared_numbers(-3, 3))


if __name__ == '__main__':
    main()