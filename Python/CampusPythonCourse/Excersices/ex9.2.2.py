def copy_file_content(source, destination):
    """
    Function that copy content in one file to another
    :param source: file we copy from
    :param destination: file we copy to
    :return: None
    """
    file_source = open(source, "r")
    file_destination = open(destination, 'w')
    for line in file_source:
        file_destination.write(line)

    file_source.close()
    file_destination.close()


def main():
    copy_file_content(r"d:\copy.txt", r"d:\paste.txt")


if __name__ == '__main__':
    main()