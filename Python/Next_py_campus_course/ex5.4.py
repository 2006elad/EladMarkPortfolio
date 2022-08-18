import itertools


class IDIterator:
    def __init__(self, user_id=99999999):
        self._id = user_id + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._id + 1 == 1000000000:
            raise StopIteration
        self._id += 1
        return self._id


def id_generator(user_id):
    for current_id in itertools.count(user_id + 1):
        if current_id == 1000000000:
            break
        yield current_id


def check_id_valid(id_number):
    # if not isinstance(id_number, int) or len(str(id_number)) != 9:
    #     return False
    # else:
        id_number_check_valid_list = [list(map(int, str(id_number))), [1, 2, 1, 2, 1, 2, 1, 2, 1]]
        id_number_check_valid_list.append([x * y for x, y in zip(id_number_check_valid_list[0], id_number_check_valid_list[1])])
        id_number_check_valid_list.append([x % 10 + x // 10 for x in id_number_check_valid_list[2]])
        if sum(id_number_check_valid_list[3]) % 10 == 0:
            return True
        else:
            return False


def main():
    user_id = int(input("Please input valid id(number with 9 length): "))
    user_choice = input("Generator or Iterator? (gen/it)? ")
    count_valid_id = 0
    if user_choice.lower == "it":
        id_chosen_choice_method = IDIterator(user_id)
    else:
        id_chosen_choice_method = id_generator(user_id)
    for current_id in id_chosen_choice_method:
        if count_valid_id == 10:
            break
        if check_id_valid(current_id):
            print(current_id)
            count_valid_id += 1


if __name__ == '__main__':
    main()
