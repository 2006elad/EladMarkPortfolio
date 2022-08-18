import functools


def add_letter(x, y): return x + y + y


def double_letter(my_str):
    """
    Function that double each letter
    :param my_str: the string
    :return:
    """
    return "".join(functools.reduce(add_letter, list(my_str), ""))


def main():
    print(double_letter("python"))
    print(double_letter("we are the champions!"))


if __name__ == '__main__':
    main()