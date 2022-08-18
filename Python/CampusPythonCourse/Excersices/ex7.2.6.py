def menu_choice_validation():
    """
    Function that validate that choice is between 1-9
    :return: the validated choice
    :rtype: int
    """
    print("""\n\nPlease choose choice between 1-9:
        1 - Print purchase products list
        2 - Print num of products in list
        3 - Search and print if product is included in the list
        4 - Count how many time a product is appear in the list
        5 - Remove product from the list
        6 - Add product to the list
        7 - Print all of the unvalidated product in list (less than 3 letter or include non alpha letters)
        8 - Remove all duplicate product
        9 - Exit      
    """)
    print("Write you choice here:")
    choice = ""
    is_valid = False
    while not is_valid:
        try:
            choice = int(input())
        except ValueError:
            print("You can enter only digits")
        else:
            if 1 <= choice <= 9:
                is_valid = True
            else:
                print("You can only enter choice that are between 1-9\nPlease enter again: ")
    return choice


def main():
    """
    Supermarket function with menu
    :return:None
    """
    print("Welcome to supermarket program")
    product_string = input("Please insert the list of the product: ")
    product_list = product_string.split(",")
    finish_flag = False
    while not finish_flag:
        choice = menu_choice_validation()
        if choice == 1:
            print("~~~~Product list~~~~")
            for item in product_list:
                print("*", item)
        elif choice == 2:
            print("There is", len(product_list), "in the products list")
        elif choice == 3:
            item_to_search = input("Please insert the product you want to find: ")
            if item_to_search in product_list:
                print("The product is inside the list")
            else:
                print("The product isn't inside the list")
        elif choice == 4:
            item_to_count = input("Please insert the product you want to count: ")
            print("The times the item you insert in the list is ", product_list.count(item_to_count))
        elif choice == 5:
            item_to_remove = input("Please insert the product you want to remove: ")
            if item_to_remove in product_list:
                product_list.remove(item_to_remove)
                print("Product has been removed from the list")
            else:
                print("Product isn't found")
        elif choice == 6:
            item_to_add = input("Please insert the product you want to add: ")
            product_list.append(item_to_add)
        elif choice == 7:
            print("~~~Unvalidated list~~~")
            for item in product_list:
                if len(item) < 3 or not item.isalpha():
                    print(item)
        elif choice == 8:
            product_list.sort()
            temp_list = []
            for i in range(1, len(product_list)):
                if product_list[i - 1] != product_list[i]:
                    temp_list.append(product_list[i])
            product_list = temp_list.copy()
            print("Duplicate item has been removed")
        elif choice == 9:
            finish_flag = True
    print("Bye Bye")


if __name__ == '__main__':
    main()