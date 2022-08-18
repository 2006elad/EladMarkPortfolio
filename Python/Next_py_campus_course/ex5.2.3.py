import itertools


def main():
    wallet = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
    count_iteration = itertools.count(1)
    count = next(count_iteration)
    opt_list = []
    while count < len(wallet):
        for one_opt in set(itertools.combinations(wallet, count)):
            if sum(one_opt) == 100:
                opt_list.append(one_opt)
        count = next(count_iteration)
    print(len(opt_list))


if __name__ == '__main__':
    main()

