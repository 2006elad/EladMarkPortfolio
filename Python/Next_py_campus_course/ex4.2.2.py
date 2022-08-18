def parse_ranges(ranges_string):
    """
    Function that gets a string of ranges that seperate with ",". The range is send back the numbers that are in the ranges
    :param ranges_string:the range string
    :type: str
    :return:The list of numbers that are in the range
    """
    only_ranges_gen = (one_range.split("-") for one_range in ranges_string.split(","))
    return (n for i in only_ranges_gen for n in range(int(i[0]), int(i[1]) + 1))


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == '__main__':
    main()
