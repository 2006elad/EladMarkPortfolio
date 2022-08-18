def filter_four(number):
    if number % 4 == 0:
        return number


def four_dividers(number):
    """
    Function that return all numbers in range that divided by four
    :param number: range number
    :type number: int
    :return: list of numbers
    :rtype: list
    """
    return list(filter(filter_four, range(number)))


def main():
    print(four_dividers(9))
    print(four_dividers(3))


if __name__ == '__main__':
    main()
