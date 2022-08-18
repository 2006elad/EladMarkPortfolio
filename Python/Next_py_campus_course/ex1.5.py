def the_longest_name(names_list):
    print(max(names_list, key=len))


def total_letter_is_file(names_list):
    print(sum([len(name) for name in names_list]))


def the_shortest_names(names_list):
    min_len = len(min(names_list, key=len))
    right_name_list = list(filter(lambda x: x is not None, [name if len(name) == min_len
                                                            else None for name in names_list]))
    print("\n".join(right_name_list))


def names_length_new_file(names_list):
    with open('name_length.txt', 'w') as new_file:
        names_length_list = [str(len(name)) for name in names_list]
        new_file.writelines("\n".join(names_length_list))


def find_names_by_length(name_list):
    wanted_length = int(input("Enter name length:"))
    right_length_name_list = [name if len(name) == wanted_length else None for name in name_list]
    print("\n".join(list(filter(lambda x: x is not None, right_length_name_list))))


def main():
    names_file = open('names.txt', 'r')
    names_list = names_file.readlines()
    for i in range(len(names_list)):
        names_list[i] = names_list[i].strip("\n")

    is_finish = False
    while not is_finish:
        choice = int(input("""Please make a choice:
        1- for the longest name
        2 - to find the total length of names
        3 - to find the shortest names
        4 - create new file with all of the name length in their line in file
        5 - find names that are in the length user input
        6 to exit
        Please input here: """))
        if choice == 1:
            the_longest_name(names_list)
        elif choice == 2:
            total_letter_is_file(names_list)
        elif choice == 3:
            the_shortest_names(names_list)
        elif choice == 4:
            names_length_new_file(names_list)
        elif choice == 5:
            find_names_by_length(names_list)
        else:
            is_finish = True
    names_file.close()


if __name__ == '__main__':
    main()
