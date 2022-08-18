#   Paragraph 2A function - Create grade list between 1-100 by num of students
def ask_for_grades(num_of_students):
    students_grade_list = [-1] * num_of_students    # Create the default list to input by num of students

    for i in range(num_of_students):  # Input grade by the num of students
        while students_grade_list[i] < 0 or students_grade_list[i] > 100:
            while True:
                try:
                    students_grade_list[i] = int(input("Please enter the grade of students number " +
                                                       str(i + 1) + ": "))
                    break
                except ValueError:  # Input Validations
                    print("Please insert only Integers")

            if students_grade_list[i] < 0 or students_grade_list[i] > 100:
                print("Please insert grade only between 0-100")
    return students_grade_list


def calc_average(students_grade_list):  # Paragraph 2B function - calculate average
    sum_of_num = 0

    for grade in students_grade_list:
        sum_of_num += grade

    return sum_of_num / len(students_grade_list)


def range_grade(students_grade_list, i, j): # Function 2C - print students grade by indexes
    if i > j:
        for x in range(i - 1, j - 2, -1):
            print("The grade of student number: " + str(x + 1) + " is: " + str(students_grade_list[x]))
    else:
        for x in range(i - 1, j, 1):
            print("The grade of student number: " + str(x + 1) + " is: " + str(students_grade_list[x]))


def calc_grade(students_grade_list):    # Paragraph 2D function - add factor to grades if needed
    average = calc_average(students_grade_list)
    if average < 70:
        factor = 70 - average
        for i in range(len(students_grade_list)):
            if students_grade_list[i] + factor >= 100:  # If the grade is above 100 then we change grade to 100
                students_grade_list[i] = 100
            else:
                students_grade_list[i] += factor

    return students_grade_list


# Sub main Function
def menu_validation():  # Sum main Function that input and validate menu choice number for printing grade
    user_choice = -1
    while user_choice < 0 or user_choice > 2:
        while True:
            try:
                user_choice = int(input())
                break
            except ValueError:  # choice Validations
                print("You can enter only integers")

        if user_choice < 0:
            print("Please insert Positive number")

        if user_choice > 2:
            print("Please enter only the choices number that above")

    return user_choice


#   Sub main function that input and validated students min or max indexes
def index_number_validation(max_length):
    index_number = -1
    while index_number < 0 or index_number > max_length:
        while True:
            try:
                index_number = int(input())
                break
            except ValueError:  # Index Validations
                print("You can enter only integers\nPlease insert index number again:")

        if index_number < 0:
            print("Please insert Positive number\nYou can insert only numbers between 0 - " + str(max_length) +
                  "\nPlease insert number again:")

        if index_number > max_length:
            print("You can insert only numbers  between 0 - " + str(max_length) + "\nPlease insert the Number Again")

    return index_number


# Main
num_of_students = int(input("Please insert the number of students: "))
students_grade_list = ask_for_grades(num_of_students)
for x in range(len(students_grade_list)):   # For loop that print students grade
    print("The grade of student number " + str(x + 1) + "  is: " + str(students_grade_list[x]))

students_grade_list = calc_grade(students_grade_list)

exit_program = False    # Stop program flag
while not exit_program:
    print("\n\nPrint grades Menu:\nIf you want to print all the grades - Press 1\n" +   #  print menu options
          "If you want to print specific students grades by indexes - Press 2\nIf you want to exit program - Press 0")
    choice = menu_validation()
    if choice == 1:     # If the user want to print all grades
        range_grade(students_grade_list, 1, len(students_grade_list))
    elif choice == 2:   # If user want to print specific students grades
        print("Please insert indexes you want to print - You can enter between 1-" +
              str(len(students_grade_list)))
        print("Please insert the first student you want to print:")
        from_index = index_number_validation(len(students_grade_list))
        print("Please insert the last student you want to print:")
        to_index = index_number_validation(len(students_grade_list))
        range_grade(students_grade_list, from_index, to_index)
    else:   # If he insert 0 and want to exit the program
        exit_program = True
        print("Bye Bye")
