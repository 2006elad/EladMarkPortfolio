def get_fibo():
    """
    Generator function of fibonatchi seq
    :return: each time one fibo value
    """
    x, y = 0, 1
    yield x
    while True:
        y, x = x + y, y
        yield x


def main():
    fibo_gen = get_fibo()
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))
    print(next(fibo_gen))


if __name__ == '__main__':
    main()