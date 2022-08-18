def chocolate_maker(small, big, x):
    """
    This program check if we have enough chocolate squares
    :param small: small chocolate squares
    :param big: big chocolate squares
    :param x: total chocolate squares we need
    :type small: int
    :type big: int
    :type x: int
    :return: True if we have enough chocolate squares, else False
    :rtype: bool
    """
    if (x // 5) - big <= 0:
        x = x - (5 * big)
        if x - small <= 0:
            return True
    return False


def main():
    print(chocolate_maker(3, 2, 10))
    print(help(chocolate_maker))
    print(chocolate_maker.__doc__)


if __name__ == "__main__":
    main()