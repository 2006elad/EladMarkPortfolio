import itertools


def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    for n in itertools.count(n):
        if is_prime(n):
            break

    return n


def main():
    print(first_prime_over(1000000))


if __name__ == '__main__':
    main()
