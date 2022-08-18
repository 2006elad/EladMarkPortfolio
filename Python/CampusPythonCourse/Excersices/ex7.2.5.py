def sequence_del(my_str):
    """
    Function that remove duplicate letters(same letters after letter appear)
    :param my_str:The string we adjust
    :type my_str: str
    :return:New string after adjustment
    :rtype: str
    """
    new_str = my_str[0]
    for i in range(1, len(my_str)):
        if my_str[i-1] != my_str[i]:
            new_str += my_str[i]
    return new_str


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))


if __name__ == '__main__':
    main()
