def arrow(my_char, max_length):
    """
    Function that create a arrow with the chosen char by the user created with the max length
    :param my_char: The char that user want to create the arrow shape with
    :param max_length: The biggest line for the arrow
    :type my_char: str
    :type max_length: int
    :return: return arrow shape string
    :rtype: str
    """
    shape_str = ""
    for i in range(1, max_length):
        if i + 1 != max_length:
            shape_str += (my_char + " ") * (i - 1)
            shape_str += my_char + '\n'
    for i in range(max_length, 0, -1):
        shape_str += (my_char + " ") * (i - 1)
        shape_str += my_char + '\n'
    return shape_str


def main():
    print(arrow('*', 5))


if __name__ == '__main__':
    main()
