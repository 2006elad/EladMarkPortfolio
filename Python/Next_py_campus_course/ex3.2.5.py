def read_file(file_name):
    """
    Function that check if file is found and return the file print style
    :param file_name: the file name
    :type: str
    :return: the new file content
    :rtype: str
    """
    file_content = ""
    try:
        file_content += "__CONTENT_START__\n"
        open(file_name, 'r')
    except IOError:
        file_content += "__NO_SUCH_FILE__\n"
    else:
        file_content += "This is the content from the file!\n"
    finally:
        file_content += "__CONTENT_END__"
        return file_content


def main():
    print(read_file("one_lined_file.txt"))
    print(read_file("file_does_not_exist.txt"))


if __name__ == '__main__':
    main()
