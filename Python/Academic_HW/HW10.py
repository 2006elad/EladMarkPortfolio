import matplotlib.pyplot as plt
import sys
import time


# Function that input the student details(with id, code courses and grades) and return the dict after the input
def dict_input(num_of_students):
    global course_code, student_id
    students_dict = {}
    for i in range(num_of_students):    # Loop that input id and insert them as keys inside the student dict
        print("\n~~~~Inputting the details of student Number " + str(i+1) + " ~~~~~~~~")

        is_student_id_new = False
        # Loop until we know the id new and isn't inputted before,
        # to make sure we have input the right num of students - as inputted
        while not is_student_id_new:
            student_id = id_validation()
            if student_id not in students_dict:   # If the id new in student dict
                students_dict[student_id] = {}  # Insert new student in the dict
                is_student_id_new = True
            else:
                print("The id is already inserted - please try again !")

        print("\n\n>>>>>>>Inputting the course codes and grades for Student with the ID: " + student_id + " <<<<<<<")

        stop_to_input = False
        # Loop that loop until the user finish to input the course codes and grades,for the current student we input
        while not stop_to_input:

            is_course_code_new = False
            # Loop that check if the course code for the specific student is new,
            # (To make sure we are not overwrite any grade that the user inserted before)
            while not is_course_code_new:
                print("Please enter new course code: ")
                course_code = str(number_validation())
                if course_code not in students_dict[student_id]:    # If the course code is new for this student
                    is_course_code_new = True
                else:
                    print("this course grade has already inserted in this student")

            # Input grades for a specific student for a specific course
            print("Please enter the grade in course: " + course_code)
            grade = grade_validation()
            students_dict[student_id][course_code] = grade

            print("Does student have more courses to input?\nPress 1 to continue\npress 0 to stop\n")
            if input_menu_validation() == 0:
                stop_to_input = True

    return students_dict


def number_validation():  # Function that validated number is digit and positive return the number
    number = -1
    while number < 0:
        while True:
            try:
                number = int(input())
                break
            except ValueError:  # number Validation
                print("You can enter only integers\nPlease insert number again:")

        if number < 0:
            print("Please insert Positive number\nPlease insert number again:")

    return number


# Function that input and validated ID is with 9 digit, number only etc - return the validated ID in string
def id_validation():
    user_id = ""
    user_id_is_valid = False
    while len(user_id) != 9 or not user_id_is_valid:  # While that run until we have 9 digits and ID is validated
        user_id = input("\nPlease Enter student israel ID (9 digits): ")
        user_id_list = list(user_id)

        if user_id_list[0] == '-':  # Check if we have negative number Furthermore, if we have non digit letters
            print("\nPlease insert Positive number Only")
            del user_id_list[0]
            if not is_digit(user_id_list):
                print("Furthermore, Please enter Only integers")

        elif len(user_id_list) != 9:  # Check if the len of id is 9 digits
            print("\nPlease Enter again id, israel ID should include 9 digits")

        elif not is_digit(user_id_list):  # Check if the ID contain only numbers
            print("\nYou can enter only integers")

        else:  # If every if statement are false then we have validated ID.
            user_id_is_valid = True

    return user_id


# ID validation - Sub Functions
def is_digit(user_id_list):  # Sub Function that check if the ID contain only digits
    for x in range(len(user_id_list)):
        try:
            user_id_list[x] = int(user_id_list[x])

        except ValueError:
            return False
    return True


def input_menu_validation():  # Function that input and validate course code input menu choice number, return choice num
    user_choice = -1
    while user_choice < 0 or user_choice > 1:
        while True:
            try:
                user_choice = int(input())
                break
            except ValueError:
                print("You can enter only integers")

        if user_choice < 0:
            print("Please insert Positive number")

        if user_choice > 1:
            print("Please enter only the choices number that above")

    return user_choice


def main_menu_validation():  # Function that input and validate the main menu choice number, return choice num
    user_choice = -1
    while user_choice < 0 or user_choice > 7:
        while True:
            try:
                user_choice = int(input())
                break
            except ValueError:
                print("You can enter only integers")

        if user_choice < 0:
            print("Please insert Positive number")

        if user_choice > 7:
            print("Please enter only the choices number that above")

    return user_choice


# Sub function that input validated grade number(between 0-100),is only digit and positive return the validated grade
def grade_validation():
    grade = -1
    while grade < 0 or grade > 100:
        while True:
            try:
                grade = int(input())
                break
            except ValueError:
                print("You can enter only integers\nPlease insert grade number again:")

        if grade < 0 or grade > 100:
            print("Please insert grade only between 0-100")

    return grade


# Main menu loop function that check every user iteration that the values of the keys in student dict aren't empty
# To make sure we aren't doing any operations with empty values (We can't input again for each id new code course)
# It to prevent error if the user decide to use the course code and grade delete function for all of the student
# Return True if empty else false.
def is_dict_empty(students_dict):
    is_empty = True
    for key, values in students_dict.items():
        if values:
            is_empty = False
    return is_empty


# Function that input id and make sure the id is found in the student dict, return true if the id found else false
def input_id_and_found_in_students_dict(students_dict):
    id_found = False
    student_id = id_validation()
    while not id_found:     # Loop and input course code until the user input the correct user id
        if student_id not in students_dict:
            print("The ID you insert isn't found...\n Please try to insert again!")
            student_id = id_validation()
        elif not students_dict[student_id]:
            print("This student dictionary is empty, Please insert another student id ")
        else:
            id_found = True
    return student_id


# Function that input course code and make sure the course code is exist for a specific student
# and he has any grade in the specific course(if the course isn't has empty grade)
# To make sure we aren't doing in specific main menu choice operation on an empty grade
# return true if the id found
def input_course_code_and_found_in_id_dict(students_dict, student_id):
    course_found = False
    print("\nPlease insert Course code: ")
    course_code = str(number_validation())
    while not course_found:  # Loop and input course code until the user input the correct course code
        if course_code not in students_dict[student_id]:
            print("The course you entered isn't found...\n Please try to insert again!")
            course_code = str(number_validation())
        elif students_dict[student_id][course_code] is None:
            print("This student course grade is empty, Please insert another course code ")
        else:
            course_found = True
    return course_code


# Function that equal to the last function but adjusted for main menu update choice
# The function is input course code and make sure the course code is exist
#  for a specific student, return true if the id found (We can update an empty value for a specific course code)
def input_course_code_for_update_grade_and_found_in_id_dict(students_dict, student_id):
    course_found = False
    print("\nPlease insert Course code: ")
    course_code = str(number_validation())
    while not course_found:
        if course_code not in students_dict[student_id]:
            print("The course you entered isn't found...\n Please try to insert again!")
            course_code = str(number_validation())
        else:
            course_found = True
    return course_code


#   Choice 7 Function that creating the grade bar chart
def show_students_grade_bar(student_grade_dict):
    student_course_codes_list =[]
    student_grades_list = []

    # Loop create grade and course codes lists for the chart,
    # Furthermore - inert for the list only course codes with grade(aren't put in the list empty course code values)
    for course_code, grade in student_grade_dict.items():
        if grade is not None:
            student_course_codes_list.append(str(course_code))
            student_grades_list.append(grade)
    plt.title("Student Grades Bar chart")
    plt.xlabel("Course Codes")
    plt.ylabel("Grades")
    plt.yticks([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    plt.grid(color='#95a5a6', linestyle='--', axis='y')
    plt.bar(student_course_codes_list, student_grades_list, color='maroon', width=0.4)
    plt.show()


#  Main
print("~~~Welcome to students grade program~~~\n")

# Inserting the num of students
print("Please enter the num of the students: ")
num_of_students = 0
num_of_student_is_not_zero = False
while not num_of_student_is_not_zero:   # Run until we have positive number and bigger than 0
    num_of_students = number_validation()
    if num_of_students == 0:
        print("You minimum number of students you can input is 1\nPlease try again")
    else:
        num_of_student_is_not_zero = True

# Create and input details for the student dict, course codes dict and their values
print("\n\nLet's start to input courses codes and id grades for each students by ID\n")
students_dict = dict_input(num_of_students)

# Main Menu
exit_program = False
# Loop until the user choose to exit program or exit if all of the student id values are empty(Without any course codes)
while not exit_program and not is_dict_empty(students_dict):

    # Timer commends for printing purposes
    sys.stdout.flush()
    time.sleep(2)

    # Menu options print menu
    print("\nIf you want to print a specific student course grade - Press 1")
    print("If you want to update to a specific student his grade in specific course  - Press 2")
    print("If you want to delete for a specific student all of his grades - Press 3")
    print("If you want to delete for a specific student a specific course and his grade - Press 4")
    print("If you want to print the grade average of a specific student  - Press 5")
    print("If you want to print all the grades of a specific students - Press 6")
    print("If you want to show a grade bar chart for a specific student - Press 7")
    print("If you want to exit - Press 0")
    choice = main_menu_validation()

    student_id = input_id_and_found_in_students_dict(students_dict) # input and make sure the input id is found
    if choice == 1:  # print the grade for a specific student in specific course
        course_code = input_course_code_and_found_in_id_dict(students_dict, student_id)
        print("\nThe grade of student with the ID: " + student_id + " in course code: " + course_code + " is: " +
              str(students_dict[student_id][course_code]))

    elif choice == 2:  # update a specific student grade in a specific course
        course_code = input_course_code_for_update_grade_and_found_in_id_dict(students_dict, student_id)
        print("Please insert the updated grade of student with the ID: " + student_id + " in course code: "
              + course_code)
        updated_grade = grade_validation()
        students_dict[student_id][course_code] = updated_grade
        print("\nThe student grade in course " + str(course_code) + " has been updated\n")

    elif choice == 3:  # delete a specific student all of his grades
        if not students_dict[student_id]:
            print("The student with the id " + str(student_id) + " is already empty")
        else:
            students_dict[student_id] = {}
            print("\nAll of the grades and course has been deleted for student with the ID" + str(student_id))

    elif choice == 4:  # delete in a specific student, a specific course and his grade
        course_code = input_course_code_and_found_in_id_dict(students_dict, student_id)
        students_dict[student_id][course_code] = None
        print("\nThe grade has been cleared for student with the id " + str(student_id) + " in course with the code: " +
              course_code)

    elif choice == 5:  # print the grade average of a specific student
        sum_of_grade = 0
        for grade in students_dict[student_id].values():
            if grade is not None:
                sum_of_grade += grade

        print("\nThe average of grades for student with the ID " + student_id + " is: " +
              str(sum_of_grade / len(students_dict[student_id])))

    elif choice == 6:  # print all the grades of a specific students
        print("~~~~~~The grades of student with the ID " + student_id + " ~~~~~~\n\n")
        for course_code, course_grade in students_dict[student_id].items():
            print("\nThe grade in course code " + str(course_grade) + " is: " + str(course_grade))

    elif choice == 7:  # show a grade bar chart for a specific student
        show_students_grade_bar(students_dict[student_id])

    else:  # If user input 0 for exit the program
        print("\nBye Bye")
        exit_program = True

    if is_dict_empty(students_dict): # If all of the student id values are empty- exit the program
        print("All students course codes and grade values are empty\nWe can't continue using the program without" +
              "any values\nBye Bye")
