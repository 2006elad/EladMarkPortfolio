# ID validate function that check if the input is follow by the rules
def id_validation():
    user_id = ""
    user_id_is_valid = False
    while len(user_id) != 9 or not user_id_is_valid:    # While that run until we have 9 digits and ID is validated
        user_id = input("\nPlease Enter user israel ID (9 digits): ")
        user_id_list = list(user_id)

        if user_id_list[0] == '-':  # Check if we have negative number Furthermore, if we have non digit letters
            print("\nPlease insert Positive number Only")
            del user_id_list[0]
            if not is_digit(user_id_list):
                print("Furthermore, Please enter Only integers")

        elif len(user_id_list) != 9:    # Check if the len of id is 9 digits
            print("\nPlease Enter again id, israel ID should include 9 digits")

        elif not is_digit(user_id_list):    # Check if the ID contain only numbers
            print("\nYou can enter only integers")

        elif not id_rules_validation(user_id_list):     # Check if the ID is follow by the subject rules
            print("\nThe id isn't following the ID rules")

        else:   # If every if statement are false then we have validated ID.
            user_id_is_valid = True

    return user_id


# ID validation - Sub Functions
def is_digit(user_id_list):    # Sub Function that check if the ID contain only digits
    for x in range(len(user_id_list)):
        try:
            user_id_list[x] = int(user_id_list[x])

        except ValueError:
            return False
    return True


def id_rules_validation(user_id):   # Sub Function that the ID follow the subject rules
    id_number_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0],      # Create id list for check the rules
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for i in range(len(id_number_list[0])):     # For loop that copy the id to the id list to check
        id_number_list[0][i] = user_id[i]

    for i in range((len(id_number_list[0]) - 1), -1, -1):   # paragraph 1A
        if i % 2 == 0:
            id_number_list[1][i] = 1
        else:
            id_number_list[1][i] = 2

    for i in range(len(id_number_list[0])):     # paragraph 1B
        id_number_list[2][i] = id_number_list[0][i] * id_number_list[1][i]

    for i in range(len(id_number_list[0])):     # paragraph 1C
        if id_number_list[2][i] > 9:
            num_to_combine = id_number_list[2][i]
            id_number_list[3][i] = num_to_combine % 10
            num_to_combine = num_to_combine // 10
            id_number_list[3][i] += num_to_combine
        else:
            id_number_list[3][i] = id_number_list[2][i]

    sum_of_id_rules_number = 0
    for i in range(len(id_number_list[0])):     # paragraph 1D
        sum_of_id_rules_number += id_number_list[3][i]

    if sum_of_id_rules_number % 10 == 0:
        return True
    else:
        return False


# Main Function
user_id = id_validation()   # Start the program
print("\n\nThe user id - is validated by the rules\nYour ID is: " + user_id)    # Print the id if validated
