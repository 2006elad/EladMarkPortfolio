def are_files_equal(file1, file2):
    """
    Function that return true if two file are equal, else if not
    :param file1: file 1 to check
    :param file2: file 2 to check
    :return: True if equal, else False
    :rtype: bool
    """
    file1_view = open(file1, 'r')
    file2_view = open(file2, 'r')
    if file1_view.read() == file2_view.read():
        return True
    else:
        return False


def main():
    print(are_files_equal(r"d:\vacation.txt", r"d:\work.txt"))


if __name__ == '__main__':
    main()