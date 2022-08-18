def who_is_missing(file_name):
    """
    Function that read a line of number and identify the missing number return and write in a file
    :param file_name: dir of file
    :type file_name: strr
    :return: The missing number
    :rtype: int
    """
    with open(r'd:\found.txt', "w") as new_file:
        file_content = open(file_name, 'r')
        file_content_list = file_content.readlines()
        file_content_string = "".join(file_content_list)
        file_content_list = file_content_string.split(',')
        file_content_list = update_list_content_to_int(file_content_list)
        for i in range(1,max(file_content_list) + 1):
            if i not in file_content_list:
                new_file.write(str(i))
                return i


def update_list_content_to_int(file_content_list):
    """
    sub function that casting the string numbers to int
    :param file_content_list: the list we want to check
    :return: return the finished list
    """
    for i in range(0, len(file_content_list)):
        file_content_list[i] = int(file_content_list[i])

    return file_content_list


def main():
    print(who_is_missing(r"d:\findMe.txt"))


if __name__ == '__main__':
    main()
