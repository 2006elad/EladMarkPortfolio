import matplotlib.pyplot as plt


# Function that input in third row the differences between before diet and after diet and return the list
def create_each_one_lose_weight_list(family_weight_list):
    for i in range(len(family_weight_list[0])):
        family_weight_list[2][i] = (family_weight_list[1][i] - family_weight_list[0][i]) * -1

    return family_weight_list


def sum_of_weight(family_weight_list, list_num):    # Function that sum chosen row and return the sum
    weight_sum = 0
    for i in range(len(family_weight_list[0])):
        weight_sum += family_weight_list[list_num][i]

    return weight_sum


def min_diet(family_weight_list):   # Function that return the minimum before and after diet weight
    min_before_diet = min(family_weight_list[0])
    min_after_diet = min(family_weight_list[1])
    print("\nThe minimum weight before diet is: " + str(min_before_diet))
    print("\nThe minimum weight after diet is: " + str(min_after_diet))


def max_diet(family_weight_list):   # Function that return the maximum before and after diet weight
    max_before_diet = max(family_weight_list[0])
    max_after_diet = max(family_weight_list[1])
    print("\nThe maximum weight before diet is: " + str(max_before_diet))
    print("\nThe maximum weight after diet is: " + str(max_after_diet))


def menu_validation():  # Function that input and validate menu choice number
    user_choice = -1
    while user_choice < 0 or user_choice > 6:
        while True:
            try:
                user_choice = int(input())
                break
            except ValueError:
                print("You can enter only integers")

        if user_choice < 0:
            print("Please insert Positive number")

        if user_choice > 6:
            print("Please enter only the choices number that above")

    return user_choice


def weight_number_validation():     # Function that validated weight number is digit and positive return the weight num
    weight_number = -1
    while weight_number < 0:
        while True:
            try:
                weight_number = int(input())
                break
            except ValueError:      # Weight number Validation
                print("You can enter only integers\nPlease insert weight number again:")

        if weight_number < 0:
            print("Please insert Positive number\nPlease insert number again:")

    return weight_number


def diet_pie_plot(family_weight_lost_list):     # Function that show the family weight lost in pie plot
    slice_labels = ['1st Member', '2st Member', '3st Member', '4st Member', '5st Member']   # Pie plot labels
    plt.pie(family_weight_lost_list, labels=slice_labels)   # Pie values
    plt.title('Family weight lost pie')     # Plot title
    plt.show()


# Main
family_weight_list = [[0, 0, 0, 0, 0],      # Create weight list
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0]]

for i in range(len(family_weight_list[0])):     # For loop input list
    print("Please insert family member number " + str(i + 1) + " Before diet weight: ")
    family_weight_list[0][i] = weight_number_validation()
    print("Please insert family member number " + str(i + 1) + " after diet weight: ")
    family_weight_list[1][i] = weight_number_validation()

family_weight_list = create_each_one_lose_weight_list(family_weight_list)   # Input the lost list

exit_program = False
while not exit_program:
    # Menu option print menu
    print("\nIf you want to print the sum of all weight before diet - Press 1")
    print("If you want to print the sum of all weight after diet - Press 2")
    print("If you want to print the difference of each family member before and after diet - Press 3")
    print("If you want to print the min weight before and after diet - Press 4")
    print("If you want to print the max weight before and after diet - Press 5")
    print("If you want to print the diet pie plot of the family - Press 6")
    print("If you want to exit - Press 0")
    choice = menu_validation()

    if choice == 1:     # Print sum of all weight before diet
        print("The sum of family weight before diet is: " + str(sum_of_weight(family_weight_list, 0)))

    elif choice == 2:   # Print sum of all weight after diet
        print("The sum of family weight after diet is: " + str(sum_of_weight(family_weight_list, 1)))

    elif choice == 3:   # Print how much each one lost weight
        print("The difference between before and after diets is:\n")
        for i in range(len(family_weight_list[0])):
            print("Family member number " + str(i + 1) + " Difference is: " +
                  str(family_weight_list[2][i]))

    elif choice == 4:   # Print the minimum weights before and after diet
        min_diet(family_weight_list)

    elif choice == 5:   # Print the maximum weights before and after diet
        max_diet(family_weight_list)

    elif choice == 6:   # Show pie family weight lost pie plot
        diet_pie_plot(family_weight_list[2])

    else:   # If user input 0 for exit the program
        print("\nBye Bye")
        exit_program = True
