def order_price(products):
    return products[1]


def sort_prices(list_of_tuples):
    """
    Function that sort prices of a products
    :param list_of_tuples: list with tuples values
    :type list_of_tuples: list
    :return: ordered list
    :rtype: list
    """
    list_of_tuples.sort(key=order_price, reverse=True)
    print(list_of_tuples)


def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    sort_prices(products)


if __name__ == '__main__':
    main()