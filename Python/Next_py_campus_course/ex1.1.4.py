import functools


def sum_of_digits(number):
    """
    Function that return the sum of digits of a number
    :param number: the number to sum his digits
    :type number:int
    :return: the sum
    :rtype: int
    """
    return functools.reduce(add_numbers, list(map(int, list(str(number)))), 0)


def add_numbers(x, y): return x + y


def main():
    print(sum_of_digits(104))


if __name__ == '__main__':
    main()
