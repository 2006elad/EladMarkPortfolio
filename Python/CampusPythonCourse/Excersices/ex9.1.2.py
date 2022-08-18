def file_function(file_dir, file_operation):
    """
    Function that read file and print the file by the rules of the operation that user is input:
    sort - print all of the word as sorted list
    rev - print all of the words in reverse
    last - print the line from the end
    :param file_dir:
    :param file_oper:
    :return:
    """
    file_data = open(file_dir, 'r')
    file_data_list = file_data.readlines()
    if file_operation.lower() == "sort":
        file_words_list = "".join(file_data_list)
        file_words_list = file_words_list.split()
        file_words_list.sort()
        print(file_words_list)
    elif file_operation.lower() == "rev":
        for i in range(len(file_data_list)):
            print(file_data_list[i][::-1])

    elif file_operation.lower() == "last":
        n = int(input("Please input the line from the end you want to print: "))
        for i in range(-1, (-1 * n) - 1, -1):
            print(file_data_list[i])
    file_data.close()


def main():
    file_dir = input("Enter a file path: ")
    file_operation = input("Enter a task: ")
    file_function(file_dir, file_operation)


if __name__ == '__main__':
    main()
