

def is_prime(number):
    """
    Function that check if a number is prime
    :param number: the number we want to check
    :type: int
    :return: True if prime, else False
    :rtype: bool
    """
    return True not in [True if number % x == 0 else False for x in range(2, number)]


def main():
    print(is_prime(42))
    print(is_prime(43))


if __name__ == '__main__':
    main()