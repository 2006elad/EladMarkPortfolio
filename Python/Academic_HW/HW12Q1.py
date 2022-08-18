# C function that check if the start of the email contain both - letter and number, and also can contain dots
def is_alpha_and_num_or_dot(student_email):
    student_email = student_email[:student_email.find('@')]     # Slice the start of the email for check
    contain_digit = False   # if we have at least one digit
    contain_alpha = False   # if we have at least one letter
    # loop that run and check each letter that they are letter or digit or dots, if not return false - furthermore
    # check if it contain both - number and letter. if the string contain only one of them in the end of the function
    # return false
    for ch in student_email:
        if not ch.isalpha() and not ch.isdigit() and ch != '.':
            print("\nEmail should contain only letters, number or dots")
            return False
        else:
            if ch.isalpha():
                contain_alpha = True
            elif ch.isdigit():
                contain_digit = True
    if not contain_alpha:
        print("\nThe start of the email(before @) should contain not only digits but letters also!")
        return False
    if not contain_digit:
        print("\nThe start of the email(before @) should contain not only letter but digits also!")
        return False
    return True


# Function e that check that @ is appears only once
def at_sign_appear_once(student_email):
    count = 0
    for ch in student_email:
        if ch == '@':
            count = 1
    if count == 1:
        return True
    else:
        print("\nYou have more then one @ sign")
        return False


# d function that check if the end of email end with @mta.ac.il or @gmail.com
def end_with_check(student_email):
    student_email = student_email[student_email.find('@'):]     # slice from the string the end of the email
    student_email = student_email.lower()
    if not student_email.endswith("@mta.ac.il") and not student_email.endswith("@gmail.com"):
        print("\nThe email can only end with(after @) mta.ac.il or gmail.com")
        return False
    else:
        return True


#   Main program
print("Hello Student!\nPlease Enter your email address:")
is_valid = False
while not is_valid:     # while loop that run until the email input is validated
    student_email = input()
    if " " in student_email:    # a rule - check the email don't contain spaces
        print("\nYou can't enter spaces in email address")
        print("The email is not valid!\nPlease insert again:")

    # e function check if @ appear one (we change the order of rules check,
    # because this rule check help us in slicing in c and d rules)
    elif not at_sign_appear_once(student_email):
        print("The email is not valid!\nPlease insert again:")

    # c rule - check if the start of the email contain letter and digits (can also contain dots)
    # we change the order here also - because c help us in b rule that make sure we don't have any signs in string
    elif not is_alpha_and_num_or_dot(student_email):
        print("The email is not valid!\nPlease insert again:")
    elif not student_email[0].isalpha():    # b rule that check if the first email letter is letter
        print("\nThe first character can only contain letters")
        print("The email is not valid!\nPlease insert again:")
    elif not end_with_check(student_email):     # d rule make sure the email end with @mta.ac.il or @gmail.com
        print("The email is not valid!\nPlease insert again:")
    else:   # if the email pass all of the rules - the email validated
        is_valid = True

print("The Email is Validated")
