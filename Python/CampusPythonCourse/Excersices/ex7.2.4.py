def seven_boom(end_number):
    """
    7 boom game function
    :param end_number: the number we end in the game
    :type end_number: int
    :return: return the number that between 0 and end number, when the string "boom" appear
     when the number is a multiply of 7 or contain 7
    :rtype: list
    """
    boom_list = []
    for num in range(end_number+1):
        if num % 7 == 0 or '7' in str(num):
            boom_list.append("Boom")
        else:
            boom_list.append(num)

    return boom_list


def main():
    print(seven_boom(17))


if __name__ == '__main__':
    main()